import time
import hashlib

class blok:
    def __init__(self, timstmp, indx, pr_hash, data):
        self.timstmp = timstmp
        self.indx = indx
        self.pr_hash = pr_hash
        self.data = data
        self.nonce = 0                  # FIXED: nonce must come BEFORE hash
        self.hash = self.cmpt_hash()    # compute hash after nonce is initialized

    def cmpt_hash(self):
        blok_str = f"{self.timstmp}{self.indx}{self.pr_hash}{self.data}{self.nonce}"
        return hashlib.sha256(blok_str.encode()).hexdigest()


class blockchain:
    def __init__(self, diff=1):
        self.diff = diff
        self.chain = []           # FIXED: initialize chain BEFORE creating genesis
        self.crt_gnss_blok()

    def crt_gnss_blok(self):
        # FIXED: correct order → timestamp, index, previous_hash, data
        gnss_block = blok(time.time(), 0, "0", "Genesis block")
        self.mine_blok(gnss_block)
        self.chain.append(gnss_block)

    def get_last_blok(self):
        return self.chain[-1]

    def add_blok(self, data):
        pr_blok = self.get_last_blok()   # FIXED: added parentheses
        new_block = blok(
            timstmp=time.time(),
            indx=pr_blok.indx + 1,
            pr_hash=pr_blok.hash,
            data=data
        )
        self.mine_blok(new_block)
        self.chain.append(new_block)

    def mine_blok(self, blok):
        req_pre = "0" * self.diff
        while not blok.hash.startswith(req_pre):
            blok.nonce += 1
            blok.hash = blok.cmpt_hash()
        print(f"Block {blok.indx} mined using nonce {blok.nonce}: {blok.hash}")

    def is_valide(self):
        req_pre = "0" * self.diff

        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            pr = self.chain[i - 1]

            # 1. Check previous hash link
            if curr.pr_hash != pr.hash:
                print("❌ Matching error (previous hash link broken).")
                return False

            # 2. Check proof of work
            if not curr.hash.startswith(req_pre):
                print("❌ Proof of work error.")
                return False

            # 3. Recompute hash and check integrity
            if curr.cmpt_hash() != curr.hash:
                print("❌ Hash error (data tampered).")
                return False

        return True

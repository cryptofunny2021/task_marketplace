contract TaskMarketplace:

    def __init__(self):
        self.tasks = {}
        self.bids = {}
        self.id = 0

    def create_task(self, creator, desc, reward):
        tid = self.id
        self.id += 1

        self.tasks[tid] = {
            "creator": creator,
            "desc": desc,
            "reward": reward,
            "status": "open"
        }

        return tid

    def bid(self, tid, user, score):
        if tid not in self.bids:
            self.bids[tid] = []

        self.bids[tid].append({"user": user, "score": score})

    def assign(self, tid):
        best = max(self.bids[tid], key=lambda x: x["score"])
        self.tasks[tid]["assigned"] = best["user"]
        return best["user"]

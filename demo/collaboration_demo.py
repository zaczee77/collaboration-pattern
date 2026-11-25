"""Reference demo: shared review of deal workspace items with owners and comments.

Every sample name and item in this file is invented.
The demo models the collaboration idea described for Txvni, an AI deal
workspace that lists collaboration among its features. It is not the
Txvni product and it makes no claim about real usage or outcomes.
"""

ALLOWED_STATUSES = ["open", "in_review", "resolved"]


class CollaborationBoard:
    def __init__(self, allowed_statuses):
        self.allowed_statuses = list(allowed_statuses)
        self.items = {}
        self.comments = []
        self.rejected = []

    def add_item(self, item_id, title, owner, source):
        if item_id in self.items:
            self.rejected.append((item_id, "duplicate item"))
            return False
        if not source or not source.strip():
            self.rejected.append((item_id, "missing source"))
            return False
        if not owner or not owner.strip():
            self.rejected.append((item_id, "missing owner"))
            return False
        self.items[item_id] = {
            "title": title,
            "owner": owner,
            "assignee": owner,
            "source": source,
            "status": "open",
        }
        return True

    def assign(self, item_id, assignee):
        if item_id not in self.items:
            self.rejected.append((item_id, "unknown item"))
            return False
        if not assignee or not assignee.strip():
            self.rejected.append((item_id, "missing assignee"))
            return False
        self.items[item_id]["assignee"] = assignee
        return True

    def add_comment(self, item_id, author, text):
        if item_id not in self.items:
            self.rejected.append((item_id, "unknown item"))
            return False
        if not text or not text.strip():
            self.rejected.append((item_id, "empty comment"))
            return False
        self.comments.append(
            {"item_id": item_id, "author": author, "text": text}
        )
        return True

    def set_status(self, item_id, status):
        if item_id not in self.items:
            self.rejected.append((item_id, "unknown item"))
            return False
        if status not in self.allowed_statuses:
            self.rejected.append((item_id, "unknown status"))
            return False
        self.items[item_id]["status"] = status
        return True

    def count_by_status(self):
        counts = {}
        for status in self.allowed_statuses:
            counts[status] = 0
        for item in self.items.values():
            counts[item["status"]] += 1
        return counts


SAMPLE_ITEMS = [
    ("item_1", "Check revenue figure", "reviewer_a", "sample_financials.csv"),
    ("item_2", "Review risk note", "reviewer_b", "sample_risk_notes.md"),
    ("item_3", "Confirm benchmark source", "reviewer_a", "sample_benchmarks.md"),
    ("item_1", "Duplicate revenue check", "reviewer_b", "sample_financials.csv"),
    ("item_4", "Unsourced claim check", "reviewer_a", ""),
]

SAMPLE_COMMENTS = [
    ("item_1", "reviewer_b", "Figure matches the source table."),
    ("item_2", "reviewer_a", "Risk note needs a second source."),
    ("item_3", "reviewer_a", ""),
    ("item_9", "reviewer_a", "Comment on a missing item."),
]


def main():
    board = CollaborationBoard(ALLOWED_STATUSES)
    accepted_items = 0
    for item_id, title, owner, source in SAMPLE_ITEMS:
        if board.add_item(item_id, title, owner, source):
            accepted_items += 1

    print(f"{len(SAMPLE_ITEMS)} items received, {accepted_items} accepted, {len(board.rejected)} rejected so far")
    assert accepted_items == 3 and len(board.rejected) == 2

    assert board.assign("item_2", "reviewer_a")

    accepted_comments = 0
    for item_id, author, text in SAMPLE_COMMENTS:
        if board.add_comment(item_id, author, text):
            accepted_comments += 1

    print(f"{len(SAMPLE_COMMENTS)} comments received, {accepted_comments} accepted, {len(board.comments)} stored")
    assert accepted_comments == 2 and len(board.comments) == 2

    assert board.set_status("item_1", "resolved")
    assert board.set_status("item_2", "in_review")
    assert not board.set_status("item_3", "closed")

    counts = board.count_by_status()
    print(f"status counts: {counts}")
    assert counts == {"open": 1, "in_review": 1, "resolved": 1}

    reasons = sorted(reason for _, reason in board.rejected)
    print(f"rejection reasons: {reasons}")
    assert reasons == [
        "duplicate item",
        "empty comment",
        "missing source",
        "unknown item",
        "unknown status",
    ]

    for item_id in sorted(board.items):
        item = board.items[item_id]
        print(
            f"{item_id}: {item['title']}, owner {item['owner']}, "
            f"assignee {item['assignee']}, status {item['status']}, "
            f"source {item['source']}"
        )

    print("all checks passed")


if __name__ == "__main__":
    main()

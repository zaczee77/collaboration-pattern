# Demo: collaboration

A small reference demo of the collaboration idea behind Txvni: each workspace item names an owner and a source, comments attach to items, assignments are recorded on the item, and status changes use a fixed list of values.

## How to run it

From the repository root, or from this folder:

```
python3 demo/collaboration_demo.py
```

Plain Python, no external packages, no network calls.

## What it does

1. It feeds 5 invented items into the board, covering a revenue figure check, a risk note review, and a benchmark source check, plus one duplicate item and one item with no source.
2. It accepts 3 items and rejects 2: one item whose identifier repeats an earlier item, and one item with no source.
3. It reassigns the risk note review item, then accepts 2 of 4 comments and rejects an empty comment and a comment on an unknown item.
4. It resolves one item, moves one item to in review, and rejects a status outside the fixed list.
5. It reports final status counts of one open, one in review, and one resolved, with the owner, assignee, status, and source printed for each accepted item.

## What it printed when it was tested

5 items received, 3 accepted, and 2 rejected at creation. 4 comments received, 2 accepted, and 2 stored. Status counts of open 1, in review 1, and resolved 1. Rejection reasons duplicate item, empty comment, missing source, unknown item, and unknown status. All checks passed.

## What the sample data is

Every item, comment, reviewer name, and document name in `collaboration_demo.py` is invented sample data written only to exercise the pattern. Nothing here is a real document, a real deal, a real team, a real user, or a real decision. A real system would add accounts and permissions, notifications, real document storage, and conflict handling when two people edit at once. None of that is modeled here.

## Files

1. `collaboration_demo.py`: the demo. The fixed status list, the sample items and comments, the board, the rejection rules, and the built in assertions.
2. `README.md`: this file.

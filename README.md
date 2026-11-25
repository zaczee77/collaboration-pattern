# Collaboration pattern

A reference pattern and a small runnable demo for shared review of workspace items, where every item has an owner, an assignee, a status, a source, and a comment history. The pattern comes from work Nirmeet Rao has shipped: Txvni, his AI deal workspace for private equity, hedge fund, and family office teams, which ingests documents and spreadsheets for cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail.

## The problem

Team review breaks down when work lives in separate notes. A reader cannot tell who owns an open question, who was asked to check it, what was already said about it, or which document the question came from. The same check gets done twice, or it never gets done at all.

A shared board prevents that loss. Each item names its owner and its source when it is created. Comments attach to the item itself, assignments are recorded on the item, and status changes use a fixed list of values, so the state of the review can be read at a glance.

## What the pattern does

1. Every status that an item can hold is named in advance in a fixed list.
2. Every item names its owner and its source when it is created.
3. An item with no source is rejected and recorded as rejected, not quietly included.
4. A duplicate item identifier is rejected, so two items cannot share one identity.
5. A comment with no text is rejected, and a comment on an unknown item is rejected.
6. A status outside the fixed list is rejected, so new states cannot appear by accident.
7. The result prints the owner, the assignee, the status, and the source for every accepted item.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It feeds 5 invented items into the board. Three items are accepted, one item is rejected because it repeats an identifier already in use, and one item is rejected because it has no source. It then accepts 2 of 4 comments and reports one item open, one item in review, and one item resolved.

The docs folder describes the pattern in full: what a board item contains, why a source and an owner are required, why the status list is fixed, and what a shared board can and cannot prove.

## What this is not

This demo is not the Txvni product. It models the collaboration idea Txvni lists among its features, at miniature scale, with invented sample data. No real documents, deals, users, or outcomes appear here, and no accuracy or outcome number is claimed. A real system would add the steps this demo does not model, such as accounts and permissions, notifications, real document storage, and conflict handling when two people edit at once. None of those are modeled here.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao

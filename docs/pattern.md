# The collaboration pattern

## Where the pattern comes from

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. Its own description lists document and spreadsheet ingestion, cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail. Collaboration is the layer that lets a team work on the same extracted facts together, instead of splitting the review across separate notes and messages.

The same need appears wherever a team reviews shared work. If the owner, the assignee, the status, the source, and the comments travel with the item, a reader can see the state of the review in one step. If they do not, the state has to be rebuilt by asking around.

## The board item

A board item holds an identifier, a title, an owner, an assignee, a source name, and a status. The owner is the person responsible for the item when it is created. The assignee is the person currently asked to work on it, and it can differ from the owner after a handoff. The source name is the document the item came from, named exactly as it was ingested, so a reader can find it again. The status starts as open and moves only to values in the fixed status list.

A comment holds the item identifier, the author, and the text. Comments attach to items, not to people or to documents in general, so the discussion stays with the question it answers.

## The five rules

1. A source and an owner are required. An item with an empty source or an empty owner is rejected and the rejection is recorded with its reason. Work that cannot be traced or owned is not included quietly.
2. Identifiers are unique. An item whose identifier is already in use is rejected, so a later item cannot overwrite an earlier one by accident.
3. Comments must carry text and a real item. A comment with empty text is rejected, and a comment naming an unknown item is rejected, so discussion cannot collect in places no reader will find.
4. Statuses are fixed in advance. The board holds the list of status values it accepts, which in the demo is open, in review, and resolved. A status outside that list is rejected, so the report keeps the shape the team expects.
5. Assignment is recorded on the item. Changing who should work on an item updates the item itself, so the next reader sees the current assignee without searching messages.

## Design principles

1. Shared state beats private notes. The board is the one place that answers who owns an item, who holds it now, and what has been said about it.
2. Rejection is information. The rejected list, with reasons, tells the team exactly what work remains: find a source for one item, or remove a duplicate before it confuses the review.
3. A status is a narrow claim. It reports where an item sits in the review flow. It does not prove the underlying check was done well. That judgment stays with human review.
4. The source stays visible in the output. Printing the source with each item makes checking cheap for the reader and keeps the habit of sourcing strong for the writer.

## What the demo shows, and what it does not show

The demo shows the pattern at miniature scale: 5 invented items, 3 accepted and 2 rejected, 4 comments with 2 accepted and 2 rejected, one reassignment, and final status counts of one open, one in review, and one resolved. It does not show real accounts, real permissions, real notifications, real documents, or the Txvni product, and it claims no accuracy or outcome result. It is a reference implementation of the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao

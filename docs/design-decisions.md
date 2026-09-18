# Current Design Decisions and Limits

This document describes the existing local implementation; it introduces no code changes or service/API claims.

| Stage | Current behavior | Consequence / limit |
|---|---|---|
| Input | `pd.read_csv` with default type/NA inference | Identifier text and leading zeros are not guaranteed; default NA tokens may become missing before normalization. |
| Headings | Strip, lowercase, replace each space and hyphen with underscore | Not a general punctuation/Unicode normalizer; repeated spaces remain repeated underscores. Normalized heading collisions are not explicitly rejected. |
| Text | Object columns converted to strings and stripped; empty string and literal `nan` replaced with missing | Does not normalize case or internal whitespace in cell values; literal text can be interpreted as missing. |
| Empty rows | Drop rows whose cells are all missing | Wholly blank physical CSV lines may already have been skipped by the reader; counts describe parsed records. |
| Duplicates | Exact matches across all columns after normalization; retain first | Different raw rows may collapse after whitespace removal/type inference. No fuzzy identity matching or audit of removed source positions. |
| Required columns | Normalize requested names and check presence | Does not require every cell to be populated or validate email/date/identifier semantics. |
| Missing values | Count remaining missing cells after empty-row removal and deduplication; include only affected columns | Counts describe final rows, not the original file. No imputation or per-row rejection file. |
| Output | Direct CSV write to supplied path | Same input/output path can overwrite source; caller must use distinct paths. No immutable source copy, transactional write, or original-format preservation is guaranteed. |

## Evidence

[The synthetic example](synthetic-example.md) demonstrates normalization, deduplication, missing counts, invalid email/date retention, and leading-zero loss. Existing tests cover heading normalization, basic cleaning/export, and absent required columns; they do not prove broader semantic correctness.

## Possible later work

Explicit identifier dtypes, same-path protection, heading-collision handling, and semantic validators require implementation decisions and tests. They are not implemented in this documentation phase. An API/integration service is also outside current scope.

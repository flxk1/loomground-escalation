<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-escalation

**How much autonomy do these factors leave?**

Computes the autonomy ceiling imposed by multiple governance factors.

## Problem

Autonomy is a single setting; conflicting constraints average out. The lowest ceiling from all factors, unassessed factors at the floor.

## Install

```
pip install loomground-escalation
```

## Usage

```python
from loomground_escalation import Factor, Ladder, ceiling, autonomy_verdict
ladder = Ladder(("L0", "L1", "L2", "L3", "L4"))
esc = ceiling([Factor("data-sensitivity", "L2"), Factor("jurisdiction", "L3")], delegated="L3", ladder=ladder)
esc.granted, esc.binding, autonomy_verdict("L3", esc)
```

## Example

```
in : delegated L3 · data-sensitivity caps L2 · jurisdiction caps L3 · request at L3
out: L2 ('data-sensitivity',)
     Verdict.NOT_SATISFIED
```

## Interface

- inputs: `Ladder(levels)` ascending, caller-supplied · `Factor(name, ceiling, why)` · `delegated`
- output: `Escalation(granted, binding, delegated, ladder, factors)`; unassessed caps at `ladder.floor`
- `autonomy_verdict(requested, escalation) → Verdict` · `fold_autonomy(steps) → IssueAggregate`
- from solver: `cross_subsumption.Verdict` · `issue_aggregation.aggregate_issues`

## Family

Diagnostic operator; consumes `loomground-solver` 0.5–0.6; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-escalation`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.1.0 · 31 tests · Python >=3.10 · solver 0.5–0.6

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`

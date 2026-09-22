# SAR REM Work — refinement decisions, v0.2

Steve Brown / SAR: originating framework and intent. Private Grok review: supplied by Steve in this conversation. Implementation and independent recheck: OpenAI assistant, 22 September 2026.

## Implemented

1. Separate CONSTRAINT_BREACH from NUMERICAL_FAILURE. Nonfinite state takes precedence, even when a size limit is also exceeded. An injected nonfinite propagation result tests the simulation path.
2. Separate viscous loss from stop-projection correction. Add a seventh state component, timestamped stop events, and total_loss; update both engines, exports, UI, paper, and parity checks. The projection itself is unchanged.
3. Report period_cv only after at least two periods. This avoids presenting one period as evidence of repeatability. A single-number population CV can mathematically be zero; the null is a deliberate evidence/reporting convention.
4. Explicitly qualify justified actions as relative to Gamma and fixed U. A wrong family or false evidence can exclude the true history.
5. Align JavaScript reachable(edges,start) with the existing Python API. Grok's prose suggested the opposite argument order; the actual Python source determines this repair.
6. Execute and archive a four-timestep comparison at fixed contact stiffness, with stop-event counts. Keep its conclusions local to those settings.
7. Clarify digest verification: a self-contained hash alone cannot authenticate authorship or resist replacement of both content and digest.

## Reviewer suggestions refined rather than copied

The proposed Grok propagate fragment still added the projection correction to the combined loss field. It was not a complete separate-loss implementation. Version 0.2 completes the split across state layout, derivative, solver, summaries, UI, and exports.

The phase CV change is not a correction of an undefined arithmetic operation; it is a more cautious reporting rule.

The review's human pilot is useful as a starting point. HANDOFF_PILOT.md makes instruction equality, scoring, information asymmetry, uncertainty, and the limits of a 20-recipient pilot explicit. Comparing a trace with a richer packet tests the added bundle, not a uniquely SAR-specific mechanism. A matched-information comparator would be needed for that attribution.

## Deferred

Event-resolved/complementarity contact, elastic-stop variants, and noisy reconstruction remain separate possible extensions. No new physical mechanism or participant result is claimed. The current stop is a declared discrete approximation, not an automatically valid long-term contact law.

## Verification

26 Python tests and 16 named browser/JavaScript checks passed in this execution. The five baseline parity comparisons include loss, stop_loss, total_loss, and stop-event count. Actual receipts and timestep data are under results/. Grok's reported independent executions are not counted as our executions.

Version 0.1 was copied into a separate v0.2 working directory and left unchanged. Source snapshots retain their original version labels and assertions; the repaired companion's claim status governs its own claims.

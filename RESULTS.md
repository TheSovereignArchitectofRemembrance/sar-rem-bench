# Verification results — v0.2, 22 September 2026

Python: 26 tests passed (results/python_checks.txt). Browser/JavaScript: see results/browser_checks.json for the independently executed check list and result. Archived v0.1 receipts remain in the separate v0.1 package.

## Synthetic-model baseline

| Experiment | Closure | Maximum L (m) | Viscous loss (J) | Stop correction (J) | Residual (J) |
|---|---|---:|---:|---:|---:|
| fixed_driven | CONTINUE | 0.750000000 | 4.29403171 | 0 | 1.6494e-05 |
| compliant_driven | CONTINUE | 1.373781635 | 5.09413343 | 0.399462271 | 2.3363e-05 |
| free_oscillator | CONTINUE | 0.750000000 | 0 | 0 | -2.8999e-13 |
| damped | STABLE | 0.750000000 | 0.499998487 | 0 | 4.1612e-12 |
| breach | CONSTRAINT_BREACH | 0.751196007 | 0.000254191411 | 0 | -8.6272e-12 |

The default compliant run has four stop events. Their recorded energy corrections sum to stop_loss; total_loss = viscous loss + stop_loss. A low energy residual checks the ledger, not the accuracy of every trajectory or physical realism of the stop.

## Timestep comparison (20 seconds, kc=40 N/m)

| dt (s) | Maximum L (m) | Final x (m) | Residual (J) | Stop events |
|---|---:|---:|---:|---:|
| 0.0005 | 1.373782889 | 0.658511968 | -1.76656e-06 | 4 |
| 0.001 | 1.373782951 | 0.658511938 | 2.69439e-06 | 4 |
| 0.002 | 1.373781635 | 0.658513368 | 2.33626e-05 | 4 |
| 0.004 | 1.373797897 | 0.658505749 | 0.000255837 | 4 |

These four runs show close agreement of maximum L and final x, with larger absolute residual at the coarsest timestep. They do not prove convergence for arbitrary contact stiffness or resolve the stop at its exact physical event time.

## Scope

Recovery remains 8 → 2 → 1 in the fixed square family. Contradictory evidence abstains; duplicates add no gain. Human transfer advantage, universal STM-5 necessity, operator minimality, historical generative origins, and higher-layer physics remain open or unclaimed. The human pilot is a design only.

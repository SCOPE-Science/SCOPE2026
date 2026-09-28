# FAILED ATTEMPT — NOT A VALIDATED FINDING

This package is withdrawn from accepted findings after independent audit.

The stored matrices and replay script produce a large floating-point cross-ratio, but the package does not certify the exact mathematical object stated in the headline. The seed generators are rounded floating-point matrices and satisfy the genus-2 surface relation only approximately; no exact algebraic representation or validated interval/Newton correction is supplied. In addition, `build_matrices.py` and `replay_fallback.py` use different flag quadruples/covector conventions, so the advertised rebuild and replay paths do not compute the same observable.

The package may be useful as exploratory numerical provenance. It must not be cited as a validated exact Hitchin-representation cross-ratio theorem. A future salvage requires an exact/validated representation and a single consistent cross-ratio definition across all artifacts.

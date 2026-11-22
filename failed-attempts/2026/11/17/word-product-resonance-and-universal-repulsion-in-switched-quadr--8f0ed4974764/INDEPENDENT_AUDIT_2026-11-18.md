# Independent mathematical audit

## correctness

PASS

For x in (0,1) and t in [-1,1], q_t=x[1+t(1-x)] and 1-q_t=(1-x)(1-tx), both bracket factors strictly positive. For G_t=logit circ q_t circ sigmoid, G_t'=1+t^2 x(1-x)/([1+t(1-x)](1-tx))>=1, strict if t nonzero. Any nontrivial word makes G_w-id strictly increasing and its exact extended left/right limits are log A_w and -log B_w (including product zero and log 0=-infinity). Hence exactly one root iff both products strictly <1, with G_w'>1 at root. At a fixed point original-coordinate multiplier equals logit derivative; regular piecewise cycles are locally the same smooth word. Verified the symbolic derivative and Schwarzian S q=-6t^2/q'^2, 776 independent rational endpoint-sign word checks including extreme coefficients, and the exact rational cycle 1/5->17/50->1/5 with multiplier 27389/22440. The finite checks are corroboration only.

## originality

FAIL

Bonifant–Milnor (2006), Example 4.4, explicitly studies the IDENTICAL q_a(y)=y+a y(1-y) family for |a|<1 and notes strictly negative Schwarzian and cross-ratio expansion; Appendix B Lemma B.1 composition identity and Lemma B.2 already imply the unrestricted word-product iff criterion and repelling uniqueness by substituting the endpoint derivatives A_w and B_w. Piecewise regular cycles are the immediate local-word corollary. t=+/-1 are boundary-degenerate but follow by the elementary exact logit identity; that routine boundary extension does not salvage a distinct scientific result.

## value

FAIL

All-word repulsion and its endpoint-product criterion are direct corollaries of the general negative-Schwarzian three-fixed-point lemma already explicitly applied to q_a in a 2006 primary paper. Converting to the branch-local return map is routine. Inclusion of the derivative-zero t=+/-1 endpoints is a basic boundary algebra check, not a substantive new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.

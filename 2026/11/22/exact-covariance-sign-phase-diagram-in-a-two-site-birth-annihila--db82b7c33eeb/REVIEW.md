# Independent mathematical audit

## correctness

PASS

The state graph contains the positive-rate closed walk 00→10→01→11→10→01→00, also at r=0, so it is irreducible. I rebuilt its generator using the two separate contributions to 01→11. Principal Markov-chain-tree minors independently give the four stationary weights with total Z=(r+t)(r²+3rt+r+2t²+3t); their 2×2 cross-product difference equals tP_t(r). Z>0. P_t(0)=t³(1−2t) and the nonnegative nonconstant coefficients (with strictly positive quadratic coefficient) give strict increase on [0,∞), including t=1 where the linear term vanishes. The partial derivatives at (1/2,0) are −1/4 in t and 3/8 in r, so the root opens with slope 2/3. The large-r expansion follows by degrees. Independent replay: python3 /workspace/review_checks/2.py (SymPy); it also gives the exact rational bracket (0.3148293584778,0.3148293584779) at t=1. This is a check of the specified two-site generator, not formal verification, expert attestation or a longer-chain calculation.

## originality

PASS

The supported distinct claim is the exact reaction-dependent sign diagram for the stated two-site bond generator. The local mechanism and the reaction-free slice are not new. Inspected studies and neighboring records do not establish the active-bond root classification; a general means of computing stationary laws is not itself a sign classification.

## value

PASS

The smallest channel supporting the motivating bond reactions distinguishes positive covariance throughout from one genuine anticorrelation-to-association reversal, with a sharp boundary and an explicit rate threshold for every boundary drive in scope. This is a concrete finite benchmark for approximations that neglect neighboring occupations; a single stationary-law calculation or isolated negative covariance would not by itself supply that classification. It gives no macroscopic phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.

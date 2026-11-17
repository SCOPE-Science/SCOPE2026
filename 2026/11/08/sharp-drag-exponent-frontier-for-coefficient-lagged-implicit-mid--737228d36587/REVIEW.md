# Independent mathematical audit

## correctness

PASS

Identical a_ij=1/4 midpoint rows with equal initial stage guesses yield exact scalar Picard F_x(y)=x/[1+s(1+b y^2)^(m/2)] and unique implicit positive root. The logarithmic slope q_m(y)=m*(b y^2/(1+b y^2))*(s(1+b y^2)^(m/2)/(1+s(1+b y^2)^(m/2))) increases strictly to m. On (0,x] q_m(x)<1 for 0<m<=1, establishing true contraction in log coordinates. For m>1 the unique q_m(y_c)=1 gives a repelling fixed point when x>x_c; F_x is decreasing on [0,x], hence F_x^2 increasing and initial upper/lower subsequences monotone. Repelling r excludes coincident limits, proving real nonvanishing two-cycle. For m=2 the two-cycle equations imply yz=A/B and x=A(y+z), giving the exact pair and multiplier 4A^3/(Bx^2). Boundary x=x_c has no distinct period-two roots and converges. 50 independent bounded numerical tests agree, not a universal proof.

## originality

PASS

The nonlinear GIRK gas/dust literature supplies the exact midpoint tableau, coefficient-lagged iteration and physically important square-root Epstein–Baines drag. It does not establish, in accessible inspected descriptions, the sharp all-step m<=1 contraction versus m>1 period-two frontier for the precisely specified scalar iteration. General decreasing-map two-cycle theory is already known and not claimed as new; applying it requires exact model-specific slope identity and a complete global classification. Full primary Chen paper inaccessible through checked legitimate full-text routes; authorized Oxford returned vpn_disconnected, so this is a priority risk rather than a FAIL.

## value

PASS

The m=1 boundary is physically meaningful because it coincides with the square-root Epstein–Baines velocity correction used in real gas/dust source solvers. The unconditional convergence guarantee and exact quadratic-drag pathological two-cycle despite a unique implicit root supply a reproducible algorithmic stability boundary, not an arbitrary small test case. Scope is one scalar stage solver, not an entire simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

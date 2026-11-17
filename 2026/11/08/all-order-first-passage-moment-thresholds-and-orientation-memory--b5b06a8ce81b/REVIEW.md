# Independent mathematical audit

## correctness

PASS

In the telegraph model dot X=-1/(1+X)+v sigma, sign flips rate gamma and starts x>1/v-1, the generator backward equations yield an integrating factor (v^2(1+x)^2-1)^(-beta/2), beta=2gamma/v^2, for d_n=(m_n^+-m_n^-)/2. Monotone comparison gives nonnegative d_n; diffusive-scale martingale lower bound forces the weighted source integral to diverge if beta<=2n-1. Positive polynomial Foster–Lyapunov functions s^(2j)+(jv/gamma) sigma s^(2j-1) and compact regeneration prove finiteness if beta>2n-1. Vanishing boundary flux then yields the exact recursion C_n=1/(2^n product_{j<=n}(1-(2j-1)/beta)) for m_n~C_n x^(2n) and leading positive orientation gap 2n C_{n-1}/[v(beta-2n+1)] x^(2n-1). Independent symbolic generator/coefficient checks passed; finite-grid upwind diagnostics in package are nonproof.

## originality

PASS

PASS best of knowledge: the 2024 full primary paper on this exact logarithmic RTP supplies first-passage mean and formal all-order backward recursions, but does not establish the all-n finite-moment threshold, completed Lyapunov/integrating-factor proof or leading orientation-gap asymptotic; the separate Nov 2 published theorem covers n=2 threshold only, and these known pieces are credited. Unindexed equivalence remains risk.

## value

PASS

PASS: the hierarchy beta>2n-1 is a sharp moment phase diagram for a natural velocity-jump model, and the subleading orientation dependence is a nontrivial quantitative memory effect beyond effective-diffusion approximation. It distinguishes finite moments even when mean exists.

The dated certificate retains the supplied scientific assessment, sources and limitations.

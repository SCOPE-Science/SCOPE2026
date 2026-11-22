# Independent mathematical audit

## correctness

PASS

PASS: The specified local polynomial map has homogeneous equilibrium E=(1/S,1/S,1/S). The circulant Jacobian diagonalizes into lambda0=1-R and complex lambda±=1-R(a±ib)/S. The condition alpha^2+beta^2>alpha+beta ensures C-Sa=3/2*(alpha^2+beta^2-alpha-beta)>0, so R*=2Sa/C lies in (0,2); the complex pair crosses modulus one before the mean-mode flip at R=2 with derivative a/S>0. Bounds b^2>3a(1-a) and 0<a<1/2 imply b^2>3a^2, so |arg lambda|<pi/3 and resonances of orders 1-4 are excluded. The exact Fourier recurrence gives the center-manifold quadratic r=-2a|w|^2+..., q=-R*conj(c), d=2R*a(S+c); nonresonant quadratic elimination produces Re(conj(lambda)(d+2q conj(H)))=-2R*a^2(1+R*)<0. This universal identity was independently verified symbolically in SymPy for free a,b,S (simplifies to exactly zero difference), rather than trusting saved checker logs. Consequently the classical nonresonant Neimark-Sacker theorem yields a locally attracting shrinking invariant Jordan curve with |w|^2=(R-R*)/[2R*a S(1+R*)]+o(R-R*). Local existence does not imply positivity globally or a global basin. An explicit rational witness (alpha,beta)=(3/2,1/10) gives R*=104/151 and lambda=(143-28sqrt(3)i)/151, consistent with formula.

## originality

PASS

PASS with material historical-priority risk: Muni (2024) studies this same Euler–Lotka–Volterra cyclic system and numerically describes quasiperiodic tori, including some subcritical scenarios on other parameter routes, but no inspected theorem yields this sharp *all-admissible-first-instability* criterion and closed-form always-negative normal-form coefficient. Earlier Gardini–Lupini–Mammana–Messia (1987) specifically addresses same cyclic map and bifurcations; full text was not available via lawful OA/arXiv, and authorized Oxford access returned vpn_disconnected. That genuine inaccessible plausible source is a prominent unresolved historical risk, not automatic FAIL absent decisive coverage. Published antisymmetric circulating logistic triad has a different coupling and cannot be specialized into nonnegative alpha,beta in the specified region.

## value

PASS

PASS: Identifying the precise nonnegative competition region where oscillatory onset precedes flip, proving automatic nonresonance and an exactly negative parameter-universal Lyapunov coefficient upgrades qualitative/numerical torus observations to a rigorous analytic family theorem. Quantitative invariant-circle amplitude is a useful normal-form invariant once the Fourier normalization is fixed. The scope is a natural sharp stability boundary for a named ecological dynamical family, not an isolated numerical parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.

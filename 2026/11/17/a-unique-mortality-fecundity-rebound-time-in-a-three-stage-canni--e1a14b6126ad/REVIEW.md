# Independent mathematical audit

## correctness

PASS

From exact equilibrium P=(m+c)/κ, Z=P/m, the Jacobian J=[[-(2+c/m),1,0],[1,−1,0],[0,1,−m]] is Hurwitz, with factors (s+m)(s+p)(s+q), p,q>0. The coupled step m→m+δ changes dx/dt by +δz and dz/dt by −δz; N′=y+cz−κxz remains parameter-free, so N′(0)=0 and exact N″(0)=δZ(m²−m−c)/m. The final equilibrium surplus is δ/κ[2−c/(m(m+δ))]. In strict wedge sqrt(c/2)<m<(1+sqrt(1+4c))/2 the initial curvature is negative and final surplus positive. Differentiating in δ gives Laplace susceptibility (Z/m)[(m²−m−c)s+(2m²−c)]/[(s+m)(s+p)(s+q)]. Its integrated time response F=(Z/m)[A h+B H], with A<0, B>0, h triple convolution of positive decaying exponentials, H=∫h. Strict log-concavity/analyticity of h makes R=H/h strictly increasing from 0 to ∞; hence exactly one transverse linear response zero. Uniform local hyperbolic attraction ensures the nonlinear solution is O(δ)e^(−γt) close to E_{m+δ}, giving eventual positive sign, while exact local curvature plus C¹ convergence exclude extra early/intermediate crossings. Every sufficiently small δ thus has exactly one crossing, converging to the implicit t*. Independent SymPy matrix inversion confirms general symbolic susceptibility and rational tests reproduce normalization. This is a coupled death-and-fertility perturbation, not mortality only.

## originality

PASS

The primary Xia–Li–Chou paper contains the identical special three-stage model and steady-state hydra derivative, so that steady-state effect and lower wedge boundary are already known. Its inspected revised Appendix F.3 does not supply the nonlinear exactly-one transient crossing or the convolution clock; neither equilibrium response nor hyperbolicity logically implies unique nonmonotone transient. The present theorem adds a dynamic, shock-local one-crossing result with a precise limiting time, rather than rebranding the known equilibrium effect.

## value

PASS

A persistent mortality intervention coupled to fecundity can have the opposite signs at early and late times. The result does not merely restate a hydra equilibrium derivative: it gives a nonempty sharp strict wedge, a time-resolved unique nonlinear crossing for every small shock, and a precise limit for when reversal occurs. Distinguishing transient under-response from sustained hydra over-response is mathematically meaningful in an established three-stage model.

The dated certificate retains the supplied scientific assessment, sources and limitations.

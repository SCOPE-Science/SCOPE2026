# Independent mathematical audit

## correctness

PASS

For the literal three-dimensional map, F²(P)=P forces the partner of (x,y,z0) to be (y,x,z1), with x=sin(z0), y=sin(z1), z0=qx+(p-r)y, z1=(p-r)x+qy. Conversely these equations suffice. For u=(x+y)/2 and v=(x-y)/2 they give u=sin(Au)cos(Bv) and v=cos(Au)sin(Bv). The strict sine bound forces u=0 even at |A|=1. The remaining equation has no nonzero solution at 0<B≤1 and exactly one positive solution when 1<B<pi: on 0<Bv≤B the sinc function decreases strictly from 1 to sin(B)/B≤1/B, with equality at the upper end only for B=pi/2. The negative root is the other phase of the same orbit. At the resonant value both phase derivatives are J0 with J0³=0, so the return Jacobian J0² is nilpotent (its square already vanishes). An iterate fixing each phase has derivative zero, and continuity of the derivative gives a local contraction in a small ball, establishing superattraction. For fixed p≠0,A and the stated transverse variation, implicit differentiation gives v'(pi/2)=0 and t=cos(Bv)=-(B-pi/2)+O((B-pi/2)²). The one-step characteristic polynomial is lambda³+rt lambda²-qt lambda-pt, and after scaling by |pt|^(1/3) the limiting polynomial has three simple unit-modulus roots. Its perturbation gives relative modulus error O(|t|^(1/3)). Evenness of cosine makes both phase Jacobians equal, so squaring the spectral radius gives the asserted leading coefficient |p|^(2/3), exponent 2/3, and continued local attraction.

## originality

PASS

The literal map is prior work. The same-day staircase result demonstrably covers the principal-lobe census on |A|<1, q,r>0 and includes the p=0 nilpotent resonance. Its earlier-treatment remark gives no identifiable independent statement for the general-p law, and the same date does not establish priority. The supported distinct contribution is the closed symmetric-parameter strip with real unrestricted coefficients, together with the map-specific resonance and quantitative transverse return-radius law for fixed nonzero p. The generic fractional splitting of a nilpotent Jordan block and the shared part of the antipodal census are not credited as new.

## value

PASS

The first sine lobe is a natural threshold region of a published nonlinear model: an exact exclusion of non-antipodal competitors and a unique real cycle are useful context, but are not independently credited where the all-lobe result already applies. The distinct quantitative payoff is the attraction law at a fully vanishing return spectrum even for p≠0, where the phase derivative has a cubic, rather than the p=0 quadratic, splitting. It tells how quickly the resonant cycle loses superattraction when B is detuned and supplies a precise benchmark not given by the known singular-subfamily sink windows or by numerical bifurcation diagrams. The closed |A|≤1 boundary and signed coefficients specify the validity of that benchmark without artificial sign restrictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

The two Fourier eigenvalues are 1 and s. Minimizing the quadratic mode by mode and discarding the constant mode reduces the objective to F(a)=[C/(a+ell)+w log(a+d)]/2 with a=s² and C=ell B. The positive secant factor log((1+d)/(a+d))/2 multiplies C tau(a)-w in F(a)-F(1). Differentiating tau gives the sign of T from the proof; T(1)=0 and T' has the sign of a+2d-ell for 0<a<1. Accordingly tau can only increase, decrease, or increase then decrease; when tau(0)<tau(1), its minimum is attained only at 0. This gives the exact endpoint tie and excludes all intermediate parameters there and below; increasing w further strictly favors 0 over every a>0. For w strictly between the printed thresholds the quadratic numerator of F' is positive at 0 and negative at 1, so precisely one simple root is in (0,1), producing a strict maximum. The endpoints retain their classifications under the homeomorphism s↦s², even though the s-derivative at 0 is zero. The strict threshold ordering is exactly the stated condition: (1+d)log(1+1/d) decreases strictly from infinity to 1, and equality cannot give an open metastability interval. At ell=B=1, d=1/100, the barrier at w=1/5 independently solves 20a²−60a+19=0 with the smaller root ≈0.3598245749. Replay the analytic checks from RESULT.md, Fourier reduction through sharp auxiliary-scale boundary. VERIFICATION.md documents supplementary finite assertions; the supplied checker was inspected, not executed. The theorem requires the stated positive scales and B>0; it makes no global classification for larger blur families or for d≥d*.

## originality

PASS

The objective and a sufficient local no-blur exclusion criterion are prior. The supported distinct contribution is the exact global endpoint-only switch and the positive-width window in which no blur is strictly locally minimizing but globally inferior, including the unique barrier. Neither the inspected propositions nor the closest indexed match supplies that classification independently.

## value

PASS

This minimal mass-preserving periodic convolution is a motivated failure case for a penalty designed to avoid identity blur. The exact global threshold demonstrates contrast extinction rather than intermediate regularization, and its separation from the local threshold explains why a local test can certify neither the global optimizer nor safe tuning. This is a usable benchmark for the stated objective, not a prediction for general image sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

FAIL

Explicit counterexample entirely within hypotheses: \(n=2,m=p=1,Q=[-1,1]\), \(K_0=B_2(0,1/4)\), \(K_u(t)=A_tK_0\) for the volume-one shear \(A_t(x,y)=(x,y+tx)\), \(-1\le t\le1\). The original \(K=A_1K_0\) has vertical chord centers \(x\), so this is precisely its Steiner linear parameter system. The \(p=1\) mixed-area definition gives \(\Pi^\circ_{Q,1}(K_0)=B_2(0,1)\); determinant-one covariance gives \(\Pi^\circ_{Q,1}(K_u(t))=A_t B_2(0,1)\). Take rotationally invariant measure \(d\nu=\mathbf1_{B_2(0,1)}dx\), a \(\gamma=\infty\)-concave density on its convex support. Polar integration with \(v=\tan\vartheta\) gives \(A_\nu(t)=|B_2\cap A_tB_2|=\int_{-\infty}^{t/2}[1+(v-t)^2]^{-1}dv+\int_{t/2}^\infty(1+v^2)^{-1}dv=\pi-2\arctan(t/2)\) for \(t\ge0\). Thus the asserted \(s_\infty=1/(nm)=1/2\) concavity of \(f=\sqrt{A_\nu}\) fails: \(f\prime\prime(t)=[tA_\nu(t)-1]/[4A_\nu(t)^{3/2}(1+t^2/4)^2]>0\) at \(t=1/2\), since \(\pi>3\) and \(2\arctan(1/4)<1/2\) imply \(A_\nu(1/2)>5/2\). The package wrongly elevates the lead source\'s convexity at fixed transverse coordinates to joint convexity over all spatial coordinates. The known Steiner endpoint monotonicity is consistent with the counterexample and is not refuted.

## originality

FAIL

The asserted universal theorem is false in a basic subcase; therefore no valid original statement is delivered for which best-of-knowledge novelty can be certified. The prior endpoint theorem is genuine but is not the false all-parameter strengthening. This is an actual mathematical refutation, not a failed search or a claim that the lead paper already contains the stronger result.

## value

FAIL

The supplied final claim cannot be valuable as a correct universal mathematical result because a basic natural sheared-disc and radially truncated measure counterexample refutes it. The diagnostic counterexample may itself motivate a future correction, but it is not the final claim under audit and does not license acceptance or a speculative repaired disposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.

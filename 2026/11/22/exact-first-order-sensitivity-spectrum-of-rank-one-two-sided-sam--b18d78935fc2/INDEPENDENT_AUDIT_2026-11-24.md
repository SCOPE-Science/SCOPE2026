# Independent mathematical audit

## correctness

PASS

The nonzero overlaps keep both projection denominators away from zero locally. At the target the two projectors are onto a and b and fix the rank-one target. Differentiate the projector onto a sampled vector: at c*a, a unit and c nonzero, only the orthogonal part of the vector variation contributes, with factor 1/c, in each off-diagonal block of the projector. Applying the product rule to the sampled Galerkin map cancels sigma and gives the tangent output (e11,e12+p^T Z,e21+Zq), with normal output zero, where p=u_perp/(a^T u), q=v_perp/(b^T v). Rotate the two complement bases so p and q lie along their first axes, using arbitrary such axes for zero p or q. The row and column tangent coordinates away from those axes each receive a distinct normal coordinate with coefficients alpha or beta, respectively, giving singular values sqrt(1+alpha^2) n-2 times and sqrt(1+beta^2) m-2 times. The two axial tangent coordinates receive one shared normal coordinate with coefficients alpha and beta, giving the two eigenvalues 1 and 1+alpha^2+beta^2 of their squared singular-value matrix. The scalar coordinate gives another 1, and the identity on tangent inputs fixes the rank at m+n-1, leaving (m-1)(n-1) zero singular values. This argument includes zero misalignments, both dimensions equal to two, and coincident bands. If s=sqrt(alpha^2+beta^2)>0, take a unit normal Z along the outer product of the two first axes, and T=[p^T Z,Zq]/s in the tangent off-diagonal pair. Input (T,sZ) attains amplification sqrt(1+s^2) for the derivative, and the Fréchet remainder transfers this to the claimed local supremum limit. With s=0 any unit tangent direction attains one. Independently checked 150 full central-difference spectra of the nonlinear map in rotated coordinates with signed overlaps, zero and nonzero alignment losses, and multiple scales. Replay: python3 /workspace/independent_replays.py 1.

## originality

PASS

Zhang and the Epperly/Stewart projection sources establish antecedents for the map itself, not the exact derivative spectrum. Zhang's bound concerns finite errors and is not sharp for the infinitesimal question. A close oblique tangent projector has different linear action, with a scalar normal-to-tangent coupling absent from this map. The inspected primary and Resultary statements do not cover the claimed fixed-sketch Frobenius spectrum; absolute priority is not established.

## value

PASS

The exact local amplification is a meaningful benchmark for fixed-increment sampled low-rank updates, distinct from a sufficient finite-error bound. The spectrum identifies which perturbation directions amplify, shows that the two alignment losses enter through a coupled band rather than a product, and recovers local norm one exactly when both bases are aligned. The natural rank-one case exposes the mechanism without claiming nonlinear or higher-rank stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

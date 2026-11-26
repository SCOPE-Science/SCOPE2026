---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Below z=1/2 the scalar characteristic roots are positive and the interpolation from the smaller root gives a positive solution since e^-z>r_- and r_+>r_-. At z=1/2 the repeated-root solution has positive bracket 1+k(2e^(-1/2)-1). Above 1/2 the conjugate-root solution has positive amplitude and cosine phase F_k=k theta-arctan((a e^-z-2)/sqrt(b)), with a=3+2z and b=2z-1. Writing E=e^-z and D=b+(aE-2)^2=a-4aE+a^2E^2, the numerator of theta'-phi' over a sqrt(b)D simplifies to 2a^2 E(E+z-1), strictly positive by E>1-z. Thus F_k increases from the excluded -π/2 to the excluded kπ/2, crossing exactly floor(k/2) odd half-period targets transversely. Since g_k(0)=1, the signs alternate, giving the stated negative components and parity for the tail. On an unweighted n-vertex star, the hub basis vector splits into squared masses 1/n at eigenvalue 0 and (n-1)/n at n. A large enough finite n shifts each of the finitely many selected negative samples to a negative hub value, while the separating scalar roots give 1/n, and both step endpoints have positive limits. This proves at least the stated number of bounded components (no fixed-star uniformity claimed). The unique g_2 minimum at e^{z_*}=10+4z_* equals -1/(5+2z_*); 3<z_*<3.5 gives -1/11<m_*<-1/12. The spectral mass at zero is 1/n at each vertex of any connected symmetric weighted Laplacian, so (1+(n-1)m_*)/n is a strict positive lower bound through n=12 in the sense that this bound itself is positive. The 13-star at h=3/13 gives (16e^-3-1)/39<0, and equality in the spectral bound requires the nonconstant component to be a single eigenvector, equivalent to equal positive conductances from the given vertex to every other vertex at the stated scaling. Independent replay: python3 /workspace/checks/frozen_replay.py 4; scaled scalar recurrence sign counts sampled over a fixed log grid through stage 40, and rational Taylor enclosures certify e^3>16, e^3<22 and e^3.5>24. The phase proof, not the grid, gives the all-stage count.

## originality

PASS

The supported distinct contribution is the exact fixed-stage timestep zero count for classical constant-step BDF2 with exponential startup, its separated negativity-window consequence on finite stars, and the sharp stage-two 12/13 diagonal cutoff. Characteristic-root analysis and spectral diagonal extremization are precedented methods, not independent originality claims.

## value

PASS

An exact sign count for a standard integrator with a natural starter answers a question not captured by absolute stability. The graph consequence shows positivity of even a diagonal entry can be lost and recovered repeatedly as step size varies at one stage, and a sharp minimal graph order at the first BDF2 stage gives a reproducible benchmark. It does not claim universal entrywise positivity at small graph orders, or exactly that many star windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Decompose into the scalar root and k regular components, with top row equal to the sum of the local-root evaluations. For lambda!=0 the scalar coordinate can always be chosen after solving the lower equations; for lambda=0 a component root basis vector in ker B_j corrects the remaining scalar target. Since B_j B_j*=b_j I, B_j*/b_j gives a convergent geometric right inverse for |lambda|<sqrt(b_j); the ordinary resolvent Neumann series works outside. On the boundary write lambda=c z with c=sqrt(b_j), |z|=1. An independent explicit omitted target in the reducing radial block cB is y_n=c*z^(n+1)/(n+1), which is square-summable. If (cB-lambda)x=y, then z^(-n-1)x_(n+1)-z^(-n)x_n=1/(n+1), so the dephased coefficients are x_0+H_n and cannot be square-summable. Orthogonal projection to the radial block would turn any full solution into a radial solution. Thus the lower block obstruction survives the join exactly at each critical circle. The adjoint equation forces every coefficient to vanish by depth induction for lambda!=0, and leaflessness gives the same at zero, proving dense range. The largest regular component has degree b_k>=2. Its pairwise disjoint antichain subtrees supply orthogonal plus/minus child differences with bottom-level cancellation, so the wavelet span really reduces the joined operator. Normalized propagation gives sqrt(b_k) times an infinite-multiplicity backward shift. Inside the outer disk its translations are onto on this span and have infinitely many independent eigenvectors, so Caradus applies there and universality passes to the full operator. At and above the boundary, an assumed nonzero component coefficient forces squared mass on successive disjoint descendant levels at least (|lambda|^2/b_j)^n times its initial squared mass; contradiction. The scalar root equation then gives injectivity, ruling out restriction to a model with kernel. Spectrum follows from the open eigenvalue disk and closure together with the norm bound. S^n(S*)^n is diagonal with the depth-n descendant counts; the largest component attains b_k^n, and the root has sum b_j^(n-1)<=b_k^n. The minimum lies between min(1,k/b_1)*b_1^n and b_1^n and hence gives R_-=sqrt(b_1). Bounded finite replay: python replay/5_tree.py builds addresses explicitly, checks 20 truncations of five degree profiles (root depth at most five), and uses exact integer wavelet coefficients before normalization; 120 depth-count or difference-vector tests plus root-coupling checks passed. The frozen checker was inspected, not run; neither finite test proves infinite-dimensional range or universality.

## originality

PASS

Best of knowledge: the useful new claim is the precise coexistence of the full outer open universal disk with arbitrarily many isolated inner non-surjectivity circles on a connected unweighted tree. Standard homogeneous-shift facts, sibling cancellation, the spectral-radius bound and the Caradus criterion are not original. The located sources do not establish the joint sharp loci on this root-coupled family. Public query failure is not negative evidence.

## value

PASS

The location and geometry of the exceptional radii answer the motivating spectral-annulus problem for a natural connected family, and distinguish the full Rota-universal region from the set where the Caradus sufficient criterion applies. In particular surjectivity recovers between consecutive exceptional radii while universality never disappears anywhere in the inner disk. The exact finite but unbounded count of inner exceptions is not a consequence of knowing just the two branching-growth endpoints. No general annulus classification for arbitrary trees is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.

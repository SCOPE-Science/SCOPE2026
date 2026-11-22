# A chromatic-cycle criterion for sparse transit-depth self-calibration

## Finding
Consider an idealized multi-epoch transit experiment with unknown spot coverages and unknown, wavelength-specific intrinsic planetary transit depths, but with independently known spot/photosphere contrasts. **The exact data identify all unknowns if and only if each connected component of the epoch–band observation graph contains a cycle with nonunit observed chromatic holonomy.** This condition admits a graph-only generic test: each component must contain a cycle using at least two distinct contrast values. With at least two epochs and two distinctly contrasted bands, exactly the number of epochs plus the number of bands scalar observations is the attainable minimum for generic identification; deleting any one measurement from the minimal connected design destroys identifiability. This establishes both an exact-data distinction between observable and gauge-ambiguous campaigns and a sharp sparse measurement budget.

## Assumptions and scope
Let \(E\) be a finite nonempty set of observation epochs and \(B\) a finite nonempty set of wavelength bands. Let \(\Omega\subseteq E\times B\) be an arbitrary observation pattern and \(G\) its bipartite graph on all vertices \(E\sqcup B\), including unobserved vertices. Band contrasts \(c_j\in(0,1)\) are known; their physical meaning is the fractional reduction of cool-spot intensity relative to unspotted photospheric intensity. Unknown epoch spot coverages satisfy \(0<f_e<1\), and the constant intrinsic planetary transit depths satisfy \(0<d_j<1-c_j\). At each observed pair, the exact (noise-free) positive measured depth is
\[
D_{ej}=\frac{d_j}{1-c_j f_e},\qquad (e,j)\in\Omega.
\]
The model assumes a spotless transit chord, one uniform cool-spot contrast law, no faculae, spatial limb effects or spot-crossing signals, no intrinsic epoch-to-epoch planetary variability, and exact calibrated contrasts. The chosen strict parameter bounds keep physical depths between zero and one and make the admissible parameter set open.

Write \(Q_{ej}=1/D_{ej}\). For any simple cycle \(C=e_1-j_1-e_2-j_2-\cdots-e_r-j_r-e_1\) with \(e_{r+1}=e_1\), define the measured quantity
\[
H_C=\prod_{k=1}^{r}\frac{Q_{e_{k+1},j_k}}{Q_{e_k,j_k}}.
\]
If a graph component is a single isolated vertex, it has no cycle. Exact-data identifiability means uniqueness of the entire admissible parameter vector among solutions of these equations. Generic identifiability means uniqueness except on a proper algebraic subset of the open parameter domain (hence outside a measure-zero set).

**Theorem.** For every admissible underlying parameter vector: (i) all parameters are uniquely identified by the observations if and only if *every* connected component of \(G\) contains some simple cycle \(C\) with \(H_C\ne1\); otherwise there is a nontrivial continuous family of distinct admissible solutions. (ii) For a fixed graph and contrast labels, the observations are generically identifying if and only if every connected component has a simple cycle containing at least two distinct contrast values. (iii) If \(|E|\ge2\), \(|B|\ge2\) and at least two bands have distinct contrasts, the fewest observations in any generically identifying pattern is exactly \(|E|+|B|\), and it can be attained with a connected graph. If there is only one epoch, only one band, or every contrast is equal, no observation pattern identifies all parameters.

## Proof
**1. Propagation and cycle obstruction.** Fix any connected component, choose an epoch as root when one exists, and write its covering fraction as a free variable \(t\). If an edge in band \(j\) joins epochs \(e\) and \(e'\), eliminate their shared intrinsic depth from \(Q_{ej}d_j=1-c_jf_e\) to obtain
\[
f_{e'}=r_{ee';j}f_e+\frac{1-r_{ee';j}}{c_j},\qquad
r_{ee';j}=\frac{Q_{e'j}}{Q_{ej}}>0.
\]
Alternatively, traversing an individual epoch–band edge in either direction gives affine updates
\[
d_j=\frac{1-c_j f_e}{Q_{ej}},\qquad
f_e=\frac{1-Q_{ej}d_j}{c_j}.
\]
Thus a spanning tree expresses every unknown in the component as an affine function of \(t\), with nonzero slope along every tree edge because all contrasts and depths are positive. For an isolated band one may analogously take its intrinsic depth as the free variable. Closing a cycle applies a one-dimensional affine return map \(t\mapsto H_Ct+b_C\); the slope is the product in the definition of \(H_C\) (independent of which root in that component was used). A physically admissible solution already supplies a fixed point. If \(H_C\ne1\), the fixed point is unique, hence so are every affine-propagated covering fraction and intrinsic depth. If every cycle has \(H_C=1\), their return maps, having a fixed point and unit slope, are identities. The tree expressions then satisfy all extra edge equations for every \(t\); an open neighborhood of the original \(t\) remains physically admissible by strict positivity and the strict upper bounds. Hence an entire continuous one-parameter family survives. An acyclic component also supplies a free parameter. Components are independent, proving (i) without dimension counting or approximation.

**2. The graph-only generic condition.** Substituting the model into any cycle gives
\[
H_C=\prod_{k=1}^{r}\frac{1-c_{j_k}f_{e_{k+1}}}{1-c_{j_k}f_{e_k}}.
\]
If all contrast labels around that cycle coincide, this product telescopes to one for *every* parameter choice. Conversely, suppose two consecutive bands in a cycle have unequal contrasts. At the interior point where all covering fractions on the cycle equal some \(f_0\in(0,1)\), the logarithmic derivative with respect to the cover \(f_{e_\ell}\) at their shared epoch is
\[
\left.\frac{\partial\log H_C}{\partial f_{e_\ell}}\right|_{f_e=f_0}
=\frac{c_{j_\ell}}{1-c_{j_\ell}f_0}
-\frac{c_{j_{\ell-1}}}{1-c_{j_{\ell-1}}f_0}\ne0.
\]
So \(H_C-1\) is a nonzero rational function whose denominator is everywhere positive on the parameter domain. Its zeros lie in the zero set of a nonzero polynomial and therefore have Lebesgue measure zero. A finite union over the finitely many components is also null. If a component contains no mixed-contrast cycle, all its holonomies are identically one and (i) rules out uniqueness everywhere. This establishes (ii), including repeated contrast labels on separate monochromatic cycles.

**3. Sharp sparse cadence.** Every uniquely identifiable connected component must have at least one cycle, so it contains at least as many edges as vertices. Adding over components proves \(|\Omega|\ge|E|+|B|\). If two distinct band contrasts exist and there are at least two epochs, take all four edges of a \(K_{2,2}\) on those bands and epochs; attach every remaining band and epoch by precisely one edge to any existing opposite-type vertex. This connected spanning unicyclic graph has \(|E|+|B|\) edges, and its unique cycle is bichromatic, so it is generically identifiable by (ii). Deleting any edge makes this connected minimal design a forest, precluding identification by (i). If either side has only one vertex every observation graph is acyclic, and if all contrasts coincide every cycle telescopes. This proves (iii).

**4. Exact witness and inversion.** For two epochs and two bands choose contrasts \(c_1=1/4\), \(c_2=3/4\), spot coverages \(f_1=1/5\), \(f_2=2/5\), and intrinsic depths \(d_1=1/50\), \(d_2=1/40\). Then \((Q_{11},Q_{21},Q_{12},Q_{22})=(95/2,45,34,28)\), and
\[
H_C=\frac{45}{95/2}\frac{34}{28}=\frac{153}{133}\ne1.
\]
Set \(r_j=Q_{2j}/Q_{1j}\). The unique root is explicitly
\[
f_1=\frac{(1-r_2)/c_2-(1-r_1)/c_1}{r_1-r_2},\quad
f_2=r_1f_1+\frac{1-r_1}{c_1},\quad
d_j=\frac{1-c_jf_1}{Q_{1j}}.
\]
For data consistent with a valid model, the denominator \(r_1-r_2\) is nonzero exactly when the four-cycle holonomy differs from one.

## Verification
The companion dependency-free Python script `verify_chromatic_cycles.py` uses exact rational arithmetic. It checks the rational witness, the full affine recovery procedure on the unicyclic optimal graph with between two and seven epochs and two and six bands, the non-identifiability of the corresponding spanning tree, and a continuous gauge construction when both spectral contrasts coincide. Run with `python3 verify_chromatic_cycles.py`. It passed 31,988 exact-rational assertions during preparation. These finitely many cases are consistency tests only; the arbitrary-graph theorem follows from the proof above, not from enumeration.

## Relationship to prior work
Chakraborty et al. (first publicly available November 28, 2023; arXiv:2311.16864, subsequently A&A 685 A173) modeled evolving stellar surface contamination using realistic disk geometry, stellar rotation, limb darkening and probabilistic inversion. Their appendix contains the simplified stellar-contamination forward law; their contribution is not claimed new here. Rosich et al. (A&A 641 A82, 2020) developed time-series photometric inversion and explicitly compared the homogeneous spot forward formula with location-dependent models, while documenting a spot-contrast/filling-factor degeneracy. Rathcke et al. (arXiv:2412.16541, December 21, 2024) used a reference planet for empirical epoch-dependent correction; their design assumes an airless calibrator and does not treat arbitrary sparse epoch–band measurements under the exact single-contaminant parametric model. Ling and Strohmer (arXiv:1611.04196, 2016) studied general bilinear self-calibration and near-optimal sampling under different sensing assumptions; abstract-level evidence cannot exclude a hidden general result which implies the present specialized graph criterion. The particular contribution assessed here is the necessary-and-sufficient mixed-chromatic-cycle criterion, its exact-data exception set, the explicit sparse recovery scheme, and sharp measurement count. The absence of a matching indexed title is not proof of priority.

## Limitations
The theorem concerns exact structural identifiability only. It gives no quantitative noise conditioning, and a cycle with holonomy close to one can be extremely unstable for inference. Known contrasts are essential; treating spot temperatures or contrasts as unknown changes the model. Physical stellar surfaces contain faculae, spot crossings, limb darkening, activity evolution and wavelength-dependent geometry; realistic data will not satisfy this toy forward law exactly. The open parameter domain excludes boundary spot coverage and perfect zero-depth cases; no claims are made there. Generic uniqueness fails on the specified algebraic exceptional sets (including equal spot coverages), and disconnected designs are identifiable only when every component separately satisfies its cycle condition. This is not field validation or external mathematical certification.

## References
- H. Chakraborty, M. Lendl, B. Akinsanmi, D. J. M. Petit dit de la Roche, A. Deline, *SAGE: A tool to constrain impacts of stellar activity on transmission spectroscopy*, arXiv:2311.16864 (first public November 28, 2023); DOI: 10.1051/0004-6361/202347727. https://arxiv.org/abs/2311.16864
- A. Rosich et al., *Correcting for chromatic stellar activity effects in transits with multiband photometric monitoring: application to WASP-52*, Astronomy & Astrophysics 641 A82 (2020), DOI: 10.1051/0004-6361/202037586. https://www.aanda.org/articles/aa/pdf/2020/09/aa37586-20.pdf
- A. D. Rathcke et al., *Stellar Contamination Correction Using Back-to-Back Transits of TRAPPIST-1 b and c*, arXiv:2412.16541 (December 21, 2024). https://arxiv.org/abs/2412.16541
- S. Ling and T. Strohmer, *Self-Calibration and Bilinear Inverse Problems via Linear Least Squares*, arXiv:1611.04196 (2016), DOI: 10.1137/16M1103634. https://arxiv.org/abs/1611.04196

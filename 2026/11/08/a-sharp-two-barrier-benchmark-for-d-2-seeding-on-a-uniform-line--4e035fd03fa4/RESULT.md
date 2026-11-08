# A sharp two-barrier benchmark for \(D^2\) seeding on a uniform line

## Finding
For every integer \(n\geq 2\), let \(D_n=\{j/(n-1):0\le j<n\}\). Ordinary \(k\)-means++ with \(k=2\) chooses a uniform first center and a second input center proportional to squared distance from the first. With no subsequent Lloyd iteration, let \(\Phi_n\) be the mean squared distance of the points in \(D_n\) to their nearer selected center, and let \(\Phi_n^*\) be the minimum mean squared distance over two arbitrary real centers. Then
\[
\lim_{n\to\infty}\mathbb E\Phi_n
=\frac{11\sqrt3\pi}{1215}-\frac3{400}
=0.041763686435991\ldots,
\qquad \lim_{n\to\infty}\Phi_n^*=\frac1{48},
\]
and therefore
\[
\boxed{\lim_{n\to\infty}\frac{\mathbb E\Phi_n}{\Phi_n^*}
=\frac{176\sqrt3\pi}{405}-\frac9{25}
=2.00465694892757\ldots>2.}
\]
In particular, the expected initial seeding cost exceeds twice optimal for every sufficiently large regular one-dimensional input grid. This is a sharp, natural, two-center performance benchmark, not a worst-case optimization over all datasets.

## Assumptions and scope
The input has equally weighted points, exactly two centers, squared Euclidean distance in one dimension, sampling without replacement, and **no refinement after seeding**. The comparison optimum may choose centers anywhere in the real line, not only input points. The limit \(n\to\infty\) is a regular-grid-to-uniform-measure limit. The result concerns expected initial objective, not high-probability cost, clustering recovery, or post-Lloyd objectives.

## Proof
Set \(V(x)=\int_0^1(y-x)^2\,dy=x^2-x+1/3\). For the continuum limit, take a first center \(X\) uniform on \([0,1]\), and, conditional on \(X=x\), let the second center \(Y\) have density \((y-x)^2/V(x)\) on \([0,1]\). For fixed \(x,y\), the per-point objective is
\[
C(x,y)=\int_0^1\min\{(t-x)^2,(t-y)^2\}\,dt.
\]
Writing \(u=\min(x,y)\) and \(v=\max(x,y)\), splitting the integral at the Voronoi boundary \((u+v)/2\) gives the polynomial identity
\[
C(x,y)=\frac{3u^3+3u^2v-3uv^2-3v^3+12v^2-12v+4}{12}.
\]
Integrate separately over \(0\le y\le x\) and \(x\le y\le1\). Exact polynomial integration, with \(Q(x):=\int_0^1(y-x)^2C(x,y)\,dy\), gives
\[
Q(x)=\frac{-66x^6+198x^5-135x^4-60x^3+105x^2-42x+7}{360}.
\]
A polynomial division is the decisive identity:
\[
\frac{Q(x)}{V(x)}=
\frac{-198x^4+396x^3+57x^2-255x+41}{1080}
+\frac{11}{1620\,(x^2-x+1/3)}.
\]
The integral of the polynomial part is \(-3/400\), while completing the square yields
\[
\int_0^1\frac{dx}{x^2-x+1/3}=\frac{4\pi\sqrt3}{3}.
\]
Thus \(\mathbb E C(X,Y)=-3/400+11\sqrt3\pi/1215\), exactly as claimed.

For the continuum uniform distribution, if two ordered centers partition the interval at a Voronoi boundary \(m\), optimizing each cluster center separately gives the lower bound
\[
\int_0^1\min\{(t-a)^2,(t-b)^2\}\,dt
\ge \frac{m^3+(1-m)^3}{12}\ge\frac1{48}.
\]
The centers \(1/4,3/4\) attain equality. For discrete grids, the empirical uniform measures converge with a uniform bound on first- and second-stage sampling denominators: the normalized squared-distance denominators converge uniformly in the first center to \(V(x)\ge1/12\). Riemann sums thus pass to the joint two-center cost expectation. Independently, the empirical two-center objectives converge uniformly on the compact center square \([0,1]^2\) to the continuum objective, so their minima converge to \(1/48\). Centers outside \([0,1]\) can always be projected into it without increasing costs.

Finally, the strict inequality follows already from elementary rational bounds \(\pi>157/50\) and \(\sqrt3>433/250\): these imply \(176\sqrt3\pi/405-9/25>2\). The strict continuum inequality and convergence force the same inequality for all sufficiently large finite regular grids.

## Verification
Run the standalone standard-library program `verify.py` using `python verify.py`. The program checks the integral polynomial by independently integrating two Voronoi-region polynomials with exact rational arithmetic; confirms the quotient identity and direct integral at 627 rational inputs; confirms the polynomial integral and strict-bound certificate; independently approximates the one-dimensional and nested two-dimensional integrals; and enumerates expected finite-grid seeding costs through 129 grid points. The recorded output is in `verification_output.txt`. Finite checks corroborate the algebra and limit but are not substitutes for the analytical argument above.

## Relationship to prior work
Arthur and Vassilvitskii's classical \(k\)-means++ method introduced the \(D^2\)-weighted seeding rule; this is not a new algorithm. Bamas, Nagarajan and Svensson (first arXiv posting 20 October 2023) analyze \(D^\alpha\) seeding and obtain general approximation guarantees, with special emphasis on \(\alpha>2\) and cluster-parameter dependence. Their inspected theoretical results do not give the exact expected two-seed cost on a uniform interval. Fast and accurate \(k\)-means++ via rejection sampling studies efficient implementation rather than the planar two-seed integral. Published two-dimensional lower-bound constructions show nontrivial worst-case behavior on carefully chosen datasets but do not imply this exact uniform-line constant. The present claim is the complete explicit expectation of a canonical \(k=2\), one-dimensional, uniform-grid benchmark and the strict \(2\)-threshold. Neither a database search nor a title/abstract mismatch establishes global publication novelty; relevant undiscovered work remains possible.

## Limitations
The factor \(2.0046569\ldots\) holds only as a limit for the regular one-dimensional grid and the unrefined two-center seeding objective. It does not claim a larger worst-case bound or a practically significant improvement. The excess above two is small but exact, showing that a putative universal factor-two guarantee fails even in a noise-free uniform-line benchmark. A separate finite-grid exact formula or the effect of Lloyd refinements is not established. Published-specialist precedence has not undergone independent validation.

## References
- Etienne Bamas, Sai Ganesh Nagarajan, Ola Svensson, *An Analysis of \(D^\alpha\) seeding for \(k\)-means*, arXiv:2310.13474 (first version 20 October 2023), https://arxiv.org/abs/2310.13474.
- *Fast and Accurate k-means++ via Rejection Sampling*, arXiv:2012.11891 (2020), https://arxiv.org/abs/2012.11891.
- *Tight lower bound instances for k-means++ in two dimensions*, Theoretical Computer Science (2016), https://doi.org/10.1016/j.tcs.2016.04.012.
- David Arthur and Sergei Vassilvitskii, *k-means++: The Advantages of Careful Seeding*, SODA (2007), https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf.

# Independent mathematical audit

## correctness

PASS

Definition 2.1 of BML requires the modal relation to be a preorder containing the scope preorder. On a total chain, mutual modal reachability is therefore an equivalence relation with convex classes: if \(x<y<z\) and \(x\) is modally equivalent to \(z\), chain inclusion and transitivity force \(y\) into the same class. Distinct classes are totally ordered, so every modal preorder is exactly a contiguous-block partition, and conversely every such partition defines a preorder extending the chain. Choosing cuts in the \(n-1\) gaps gives \(2^{n-1}\). With \(\ell(d)\) the minimum of the modal block of \(d\), one has \(d\sqsubseteq e\) exactly when \(\ell(d)\le e\); intersecting this with the classifier lower bound in the primary semantic clause gives the stated suffix. The bundled finite verifier exhausts all reverse-edge choices through \(n=6\), corroborating but not replacing the general proof.

## originality

FAIL

The claim is an implication-level corollary of the defining BML conditions together with the standard classification of total preorders on a finite chain. Murase--Maniwa explicitly require the modal preorder to contain the scope preorder, and their bounded-modality semantics explicitly intersects modal reachability with the classifier lower bound. Convex blocks, the cut count \(2^{n-1}\), and the suffix formula follow by elementary order theory, so lack of this exact finite-chain wording in the source does not establish originality.

## value

FAIL

For a total chain, the entire classification reduces to the textbook fact that equivalence classes of a total preorder are consecutive blocks, followed by choosing cuts and intersecting two suffix conditions. It is a clear pedagogical normal form, but it does not constitute a separate motivated mathematical gap under the shared value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.

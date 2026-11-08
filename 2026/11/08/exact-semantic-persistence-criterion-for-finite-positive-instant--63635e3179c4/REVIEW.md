# Mathematical review

## Correctness: PASS

The claim specifies a finite poset, arbitrary upset-valued neighbourhood families, all finite arities including zero, and all valuations into upsets. Each primitive operator must preserve upsets since its arguments can be named by fresh atoms. Necessity of the box condition is proved using an argument singleton at each maximal world in the chosen witness; necessity of the diamond condition is proved using every upset failing to contain a chosen co-witness and the scope outside its down-closure. Conversely, (B) transports box witnesses through maximal points while (D) transports diamond failures through down-closures. Finiteness justifies both finite test lists and maximal-point existence. The proof includes empty-neighbourhood and zero-argument cases. An independently executed, self-contained checker corroborated 8,384 finite structural/semantic comparisons; enumeration is not the infinite-parameter proof.

## Originality: PASS, qualified

The closest primary paper is Das–Khanra–Sardar (arXiv:2606.08083v1), which defines two-sided positive instantial semantics and requires literal inclusion of the neighbourhood families as a sufficient persistence condition. It gives no inspected necessity statement or exact equivalent weaker relation. The present exact criterion properly extends the class of semantics-bearing finite frames, and a two-world example separates it from literal inclusions. Bezhanishvili–Enqvist–de Groot's 2020 classical INL duality and the finite Boolean instantial arity-recovery result address different notions (descriptive Boolean representation, respectively finite-frame recoverability). No equivalent exact criterion was identified in searches of related semantic liftings or public research records. Risk remains that an existing general ordered-neighbourhood simulation theorem implies this precise criterion; unindexed work was not exhaustively checked.

## Mathematical value: PASS

Semantic persistence is the essential well-definedness requirement for positive modal operations on the distributive lattice of upsets. The theorem identifies **all** finite two-sided neighbourhood assignments with this property, not merely a sufficient subclass. The two-world example proves that the source's syntactic persistence restrictions exclude natural admissible semantics. The conditions give a finite structural test for positive neighbourhood-frame construction and distinguish the witness/co-witness geometries. The result has uniform content across all finite posets and all modal instance arities.

## Scope and risks

The language must have enough distinct propositional variables to name each finite upset family, and all instance arities, including zero, must be admitted. The characterization is not claimed for infinite posets or for restricted-arity/language fragments. Historical priority remains conditional on the available primary literature and research-index access. The computational replay is an independent implementation check, not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.

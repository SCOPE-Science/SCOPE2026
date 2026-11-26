# Independent mathematical audit

## correctness

PASS

Let P be the announcement upset and Q the truth upset of B on the restriction, viewed in the original frame; Q remains upward closed since P is an upset. At s in P, write T=R[up(s)]. Using the stated future-world necessity, the left side tests T intersect P contained in Q, while the right tests up(T) intersect P contained in Q. Outside P each evaluation is the corresponding test over future s in P. Thus frame validity is equivalent to up(T intersect P)=up(T) intersect P for all s in P and all upsets P: necessity can already be tested with atoms p=P and q=up(T intersect P), and equality suffices for any formulas. For w in up(T) intersect P choose v>=s and vRu<=w; AR gives v'>=v and u'<=w with v'Ru' and u' above v or w. This puts u' in T intersect P. Conversely if AR fails at vRu<=w, set s=v and P=up(v) union up(w); then w lies in up(T) intersect P, but not in up(T intersect P) by absence of the AR witness. This yields the atomic countervaluation and proves all-cardinalities equivalence, including nonantisymmetric preorders and the empty announcement upset. Forward confluence witnesses AR by u'=w. On 0<1 the sole arrow 0R0 satisfies AR but violates forward confluence; the sole arrow 1R0 fails AR with p={1}, q empty. Reflexivity rules out a one-world counterexample. Independently evaluating restriction, box and implication with bitset operations (python /workspace/review-work/check-announcement.py) reproduced the all-labelled-preorder triples (1,2,2), (4,64,56), (29,14848,9571), and the fixed-chain pairs of valid and strictly nonconfluent valid counts (12,1), (224,26), (14592,1215). The finite census does not prove the unrestricted correspondence.

## originality

PASS

In the directly inspected work introducing the same arbitrary-birelational semantics, the traditional reduction is identified as not universally valid, and a different relativized-necessity equation is supplied. It does not identify the validity class of the traditional equation. The strongest indexed static correspondence and confluence findings have different hypotheses or formulas, leaving the exact AR condition, two-atom test and strict forward-confluence comparison distinct within the examined evidence.

## value

PASS

This pinpoints exactly when a named reduction remains sound after removing structural hypotheses, rather than just giving a counterexample. The equivalence with a single atomic test and the strict two-world separation make the condition usable for frame analysis and distinguish it from forward confluence. The result is an all-cardinalities correspondence, not merely a finite enumeration or a claim about full eliminability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

For distinct deletion outputs z,z′ of word w, any symbol absent from either output was deleted at its sole occurrence, hence it cannot be absent from both different outputs; therefore supp(z) union supp(z′)=supp(w). Two codewords with >=2 common distinct outputs have identical exact supports, decomposing the confusability graph into copies of seven canonical support graphs (n=3,4; support size k). Independently parsed the *actual* certificates.json Git blob and rebuilt every canonical graph directly from all words and their distinct deletion sets. In each of seven cases, verified every independent-set witness, all matching edges were genuine conflicts, all matching vertices disjoint and alpha+matching=#vertices. Exact certified alpha rows: n3 k1,2,3 ->1,4,3; n4 k1,2,3,4 ->1,8,18,12. A matching of size v-alpha gives the upper bound, independent set the lower bound. Binomial expansion yields the two formulas for ALL q>=2; finite support graphs are exhaustively certified independently of the alphabet parameter. No claims for n>=5 or identical outputs.

## originality

PASS

The exact code sizes are not determined by published general two-read deletion asymptotic constructions, the stronger one-read disjoint-ball codes, or the complete all-length confusability EDGE count. The directly relevant Cai–Kiah–Nguyen–Yaakobi paper gives definitions, q-ary reconstruction constructions and asymptotic statements, not the seven exact short-class independence numbers. The known October edge-count result cannot determine alpha(G). The all-q short-block capacity formula and matching-independent finite certificates appear independently new subject to residual unindexed finite-length-coding risk.

## value

PASS

The first two nontrivial short lengths of a natural adversarial multiread reconstruction channel have exact best code sizes for every alphabet size. Exact symbol-support decomposition and complementary graph witnesses make a useful all-q finite classification; no downstream all-length theorem is required for a meaningful sharp short-block capacity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

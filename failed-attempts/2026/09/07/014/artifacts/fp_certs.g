## fp_certs.g — Fp-presentation certificates for extremals
SizeScreen([10000, 24]);
SetPrintFormattingStatus("*stdout*", false);
Print("GAP version: ", GAPInfo.Version, " SmallGrp: ", GAPInfo.PackagesLoaded.smallgrp[2], "\n");
# S_max attainer + top-5 by s, and all K_max=60 attainers
s_top := [230, 231, 207, 209, 219];
k60_ids := [45,47,48,55,60,162,163,164,165,166,177,178,221,222,223];
ids := Union(s_top, k60_ids);
Print("certifying IDs: ", ids, "\n");
for i in ids do
  G := SmallGroup(96, i);
  Print("\n==== SmallGroup(96,", i, ") desc=", StructureDescription(G),
        " s-lattice=", Sum(ConjugacyClassesSubgroups(LatticeSubgroups(G)), Size),
        " k=", Length(ConjugacyClasses(G)),
        " ab=", IsAbelian(G), " ====\n");
  iso := IsomorphismFpGroup(G);
  F := Range(iso);
  Print("FpGroup generators: ", Length(GeneratorsOfGroup(F)), " relators: ", Length(RelatorsOfFpGroup(F)), "\n");
  Print("Relators: ", RelatorsOfFpGroup(F), "\n");
  # simplified presentation
  S := SimplifiedFpGroup(F);
  Print("Simplified: gens=", Length(GeneratorsOfGroup(S)), " rels=", Length(RelatorsOfFpGroup(S)), "\n");
  Print("Simplified relators: ", RelatorsOfFpGroup(S), "\n");
  # sanity: order check
  Print("Order(Range(iso))=", Order(F), " Order(Simplified)=", Order(S), "\n");
od;
Print("FP CERTS DONE\n");
QUIT;

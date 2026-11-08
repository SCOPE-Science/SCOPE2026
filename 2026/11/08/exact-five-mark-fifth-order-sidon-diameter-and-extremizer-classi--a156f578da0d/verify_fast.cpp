// Exact independent verifier of the least five-mark B_h diameter for h=2,3,4,5.
// Build: c++ -std=c++17 -O2 -o verify_fast verify_fast.cpp
// Run: ./verify_fast
#include <array>
#include <iostream>
#include <stdexcept>
#include <vector>

class Checker {
  std::vector<int> seen = std::vector<int>(1001, 0);
  int stamp = 0;

  bool dfs(const int *marks, int size, int length, int start, int sum) {
    if (length == 0) {
      if (seen[sum] == stamp) return false;
      seen[sum] = stamp;
      return true;
    }
    for (int i=start; i<size; ++i)
      if (!dfs(marks,size,length-1,i,sum+marks[i])) return false;
    return true;
  }

public:
  bool admissible(const int *marks, int size, int h) {
    ++stamp;
    return dfs(marks,size,h,0,0);
  }
};

int main() {
  for (int h=2; h<=5; ++h) {
    Checker checker;
    int minimum=-1, representatives=0;
    long long four_tests=0, five_tests=0;
    std::vector<std::array<int,5>> winners;
    for (int d=4; d<=72; ++d) {
      for (int a=1; a<d-2; ++a) {
        for (int b=a+1; b<d-1; ++b) {
          for (int c=b+1; c<d; ++c) {
            // Reflection reverses the gaps. At least one orientation has a<=d-c.
            if (a>d-c) continue;
            int first_four[4]={0,a,b,c};
            ++four_tests;
            if (!checker.admissible(first_four,4,h)) continue;
            ++five_tests;
            int all_five[5]={0,a,b,c,d};
            if (checker.admissible(all_five,5,h)) {
              winners.push_back({0,a,b,c,d});
              ++representatives;
            }
          }
        }
      }
      if (representatives != 0) {minimum=d;break;}
    }
    constexpr int expected[4]={11,23,41,72};
    if (minimum!=expected[h-2]) throw std::runtime_error("wrong minimum");
    std::cout << "h=" << h << " minimum=" << minimum
              << " canonical_winners=" << representatives
              << " four_checks=" << four_tests << " five_checks=" << five_tests << '\n';
    if (h==5) {
      if (representatives != 1 ||
          winners[0] != std::array<int,5>{0,1,16,66,72} ||
          four_tests != 528990 || five_tests != 139508)
        throw std::runtime_error("B5 certificate mismatch");
    }
  }
  std::cout << "VERIFY_OK\n";
}

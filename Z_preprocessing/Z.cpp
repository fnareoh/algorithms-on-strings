#include <iostream>
#include <vector>

std::vector<int> Z_algo(std::string S){
    int n = S.size();
    int r = 0;
    int l = 0;
    std::vector<int> Z(n,0);
    Z[0] = n;
    for(int k = 1; k < n; k++){
        if (k > r) {
            int z_k = 0;
            while (k+z_k < n && S[z_k]==S[k+z_k]) z_k++;
            Z[k] = z_k;
            if (z_k > 0) {
                r = k + z_k - 1;
                l = k;
            }
        }
        else {
            int k2 = k-l;
            if (Z[k2] < r-k+1) Z[k] = Z[k2];
            else {
                int z_k = r-k+1;
                while (k+z_k < n && S[z_k]==S[k+z_k]) z_k++;
                Z[k] = z_k;
                r = k + z_k - 1;
                l = k;
            }
        }
    }
    return Z;
}

int main() {
    std::string P,T;
    getline(std::cin,P);
    //getline(std::cin,T);
    std::vector<int> Z = Z_algo(P);
    for(int i = 0; i < Z.size(); i++) std::cout << i+1 << " ";
    std::cout << std::endl;
    for(int i = 0; i < Z.size(); i++) std::cout << Z[i] << " ";
    std::cout << std::endl;
}

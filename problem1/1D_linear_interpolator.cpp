#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <fstream>


using namespace std;

double binary_search_interpolator(double values[][2], double  x, int l, int r){
    if(r-l>1){
        int mid = l+ ((r-l)/2);
        if(values[mid][0]==x){
            return values[mid][1];
        }
        else if(values[mid][0] < x){
            return binary_search_interpolator(values, x, mid, r);
        }
        else{
            return binary_search_interpolator(values, x, l, mid);
        }
    }
    else{
        if(x>values[r][0] || x<values[l][0]){
            return -1;
        }
        // cout<<x<<"\n";
        return values[l][1] + (((x-values[l][0])*(values[r][1] - values[l][1]) )/(values[r][0] - values[l][0]));
    }
}

void generating_csv_for_plot(double values[][2], double interval,int n){
    ofstream MyFile("plot2.csv");
    double start = 0;
    MyFile<<"x,y\n";
    while(start<=10){
        double value = binary_search_interpolator(values,start,0,n-1);
        MyFile << start<< ","<<value<<"\n";
        start+=interval;
    }

}

int main(){
    int n = 8;
    double values[8][2] = {{0, 0.0}, {1.5707963267948966, 1.0}, {3.141592653589793, 1.2246467991473532e-16}, {4.71238898038469, -1.0}, {6.283185307179586, -2.4492935982947064e-16}, {7.853981633974483, 1.0}, {9.42477796076938, 3.6739403974420594e-16}, {10, -0.5440211108893699}};
//     cout<<binary_search_interpolator(values,3.3,0,n-1)<<"\n";
//     cout<<binary_search_interpolator(values,5,0,n-1)<<"\n";
//     cout<<binary_search_interpolator(values,0,0,n-1)<<"\n";
    generating_csv_for_plot(values,0.1,n);
}
double ReimannSum(double (*f)(double x), double start, double end, int n) {
    double sum = 0;
    double width = (end - start) / n;

    for (int i = 0; i < n; i++) {
        sum += f(start + width * i + width / 2) * width;
    }

    return sum;
}
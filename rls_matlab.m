function y = rls_filter(x, sigma2, lambda)
    N = length(x);
    u = ones(N,1);
    p = (1/sigma2)*u;
    y = zeros(N,1);
    for k = 2:N
        u = [x(k-1); u(1:end-1)];
        g = p*u/(lambda + u'*p*u);
        y(k) = u'*g;
        % Kalman gain
        p = 1/lambda*(p - g*u'*p);
    end
end
n = 1000;
m = 5*n;
x = linspace(0, 10*pi, m);
x = reshape(x, [m, 1]);
y = random('Normal', 9.8, 0.3) + sin(x);
y = random('Normal', y, 0.1);
z = zeros(m, 1);
writematrix([x,y,z],'M7.xlsx','Sheet',1,'Range','A1:C5000')
plot(x,y)
xlabel('x')
ylabel('sin(x)')
title('Plot of the Sine Function')
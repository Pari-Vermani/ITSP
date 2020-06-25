n = 1000;
x = linspace(0, 2*pi, n);
x = reshape(x, [n, 1]);
y = sin(x);
writematrix([x,y],'M7.xlsx','Sheet',1,'Range','A1:B1000')
plot(x,y)
xlabel('x')
ylabel('sin(x)')
title('Plot of the Sine Function')
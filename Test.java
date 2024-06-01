public class Test{
    public static void main(String[] args){     

        double r1 = myFunc(3.0, 3.0);
        System.out.println(r1);

        double r2 = myFunc(2.0, 3.0);
        System.out.println(r2);
        
        double r3 = myFunc(-4.0, 2.0);
        System.out.println(r3);
    }

    public static double myFunc(double x, double y){
        double result = (2 * Math.pow(x, 2)) - y + 3;
        return result;
    };
}
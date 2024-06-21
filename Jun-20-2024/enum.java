public class Main
{
    enum TournResult {
        DNQ,
        GS,
        RO16,
        QF,
        SF,
        F,
        W;
    };
    
	public static void main(String[] args) {
		System.out.println("Hello World");
		TournResult result = TournResult.DNQ;
        System.out.println(result);          // Output: DNQ
        System.out.println(result.name());   // Output: DNQ
        System.out.println(result.ordinal()); // Output: 0

        TournResult result2 = result + 1;
        System.out.println(result2);          // Output: DNQ
        System.out.println(result2.name());   // Output: DNQ
        System.out.println(result2.ordinal()); // Output: 0
	}
}

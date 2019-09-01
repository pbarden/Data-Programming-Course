/*
 * Coursework for DAT/210 - Data Programming Languages, Week 3 @ University of Phoenix
 */
package controlstructures;

// Import statements for all objects used
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.text.NumberFormat;
import java.util.Scanner;

/**
 *
 * @author Dennis Paul Barden
 */

// The primary class for this file
public class ControlStructures {

    // The main entry point using the main method, throws a FileNotFoundException as good practice just in case there's an error with the file
    public static void main(String[] args) throws FileNotFoundException {
        
        // Ask the user to enter annual sales
        System.out.println("Enter the annual sales for the employee:");
        
        // Create a new scanner object to use keyboard input
        Scanner keyboard = new Scanner(System.in);
        
        // Capture keyboard input as a double and store it
        double total_annual = keyboard.nextDouble();
        
        // Create a new Salesperson object using the annual sales entered by the user
        Salesperson employee = new Salesperson(total_annual);
        
        // Create a NumberFormat object to format output later as currency
        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance();
        
        // Display the total annual compensation on the console
        System.out.println("Total compensation for employee with " + currencyFormat.format(employee.sales) + " annual sales: " + currencyFormat.format(employee.totalCompensaion()));
        
        // Use new PrintWrtiter object to create a .txt output
        PrintWriter myPrinter = new PrintWriter("compensation_report.txt");
        
        // Print the total compensation to the new file, just like what's on the console
        myPrinter.println("Total compensation for employee with " + currencyFormat.format(employee.sales) + " annual sales: " + currencyFormat.format(employee.totalCompensaion()));
        
        // Close the file to write and finalize changes
        myPrinter.close();
    }
    
}

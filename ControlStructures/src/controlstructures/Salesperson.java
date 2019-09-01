/*
 * Coursework for DAT/210 - Data Programming Languages, Week 3 @ University of Phoenix
 */
package controlstructures;

/**
 *
 * @author paulb
 */
// Create the Salespoerson class for later use with objects in the main program (below)
public class Salesperson {
        // Fixed salary @ $30k
        final double Salary = 30000.00;
        
        // Initializes the sales amount as a double
        double sales;

        // Construct the class with name and sales amount
        Salesperson(double sales) {
            
            // Uses the constructor to set the sales amount initialized above
            this.sales = sales;
        }
        
        // Commission @ 7% of total sales
        double commission (double total_sales) {
            
            // Returns the commission value based on the total sales
            return total_sales * .07;
        }
        
        // Total compensation @ salary + commission
        double totalCompensaion () {
            
            // Returns the base salary with commision added
            return this.Salary + this.commission(sales);
        }
    }
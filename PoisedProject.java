package com.company;

import java.util.Scanner;
public class PoisedProject {
    public static ACC getData(String x){
        //we ask the user to enter data for either ACC
        System.out.println("Enter "+x+" Name here: ");
        Scanner input = new Scanner(System.in);
        String name = input.nextLine();

        System.out.println("Enter "+x+" Surname here: ");
        input = new Scanner(System.in);
        String Surname = input.nextLine();

        System.out.println("Enter "+x+" Email Address here: ");
        input = new Scanner(System.in);
        String EmailAdre = input.nextLine();

        System.out.println("Enter "+x+" telephone number here: ");
        input = new Scanner(System.in);
        String phoneNumber = input.nextLine();

        System.out.println("Enter "+x+" physical Address number here: ");
        input = new Scanner(System.in);
        String physicalAddress = input.nextLine();

        return new ACC(name,Surname,EmailAdre,phoneNumber,physicalAddress);
    }


    public static void main(String[] args) {
        //we assign x to these people
        //and ask the user the data required
        ACC Customer =getData("Customer");
        ACC Contractor =getData("Contractor");
        ACC Architect =getData("Architect");

        //we print the data for each data
        System.out.println(Customer);
        System.out.println(Contractor);
        System.out.println(Architect);

        //we ask the user fot the project data
        System.out.println("Enter Project name here or enter null: ");
        Scanner input = new Scanner(System.in);
        String PName = input.nextLine();

        System.out.println("Enter Project number here: ");
        input = new Scanner(System.in);
        String PNumber = input.nextLine();

        System.out.println("Enter Building type here: ");
        input = new Scanner(System.in);
        String BuildingT = input.nextLine();

        System.out.println("Enter Project Address here: ");
        input = new Scanner(System.in);
        String PAddress = input.nextLine();

        System.out.println("Enter ERF number here: ");
        input = new Scanner(System.in);
        String ERFnum = input.nextLine();

        System.out.println("Enter Project Cost here: ");
        input = new Scanner(System.in);
        double PFee = input.nextDouble();

        System.out.println("Enter Paid amount");
        input = new Scanner(System.in);
        double PAmount = input.nextDouble();

        System.out.println("Enter Dead line here: ");
        input = new Scanner(System.in);
        String Deadline = input.nextLine();

        //if the project name is null we print this
        if (PName.equalsIgnoreCase("null")){
            PName = BuildingT+" "+ Customer.getSurname();
        }

        Project Alpha = new Project(PName,PNumber,BuildingT,PAddress,ERFnum,PAmount,PFee,Deadline);
        System.out.println(Alpha);

        //we make a menu with options
        System.out.println("c- change due date of the task." +
                "\np- change the total amount fee paid to date." +
                "\nu- update contractors contact details." +
                "\nf- finalize project.");
        Scanner menuOp = new Scanner(System.in);
        String option = menuOp.nextLine();

        //if we choose options c
        if(option.equalsIgnoreCase("c")){
            //we ask the user for the new deadline
            System.out.println("Enter new Project deadline: ");
            Scanner answer = new Scanner(System.in);
            String NewDate = answer.nextLine();

            //we update the deadline in project
            Alpha.setDeadLine(NewDate);
            System.out.println(Alpha);
        //else if option is p
        }else if (option.equalsIgnoreCase("p")){
            //we ask the user how much was paid
            System.out.println("Enter paid amount here: ");
            Scanner ans = new Scanner(System.in);
            double SecPAmount = ans.nextDouble();
            //we update the the paid amount
            Alpha.setPaidFee(SecPAmount+PAmount);
            System.out.println(Alpha);

            double OutStanding = Alpha.getTotalAmount()-SecPAmount-PAmount;
            double PaidAmount = SecPAmount+PAmount;

            System.out.println("Paid amount: R"+PaidAmount+"\nOutstanding amount: R"+OutStanding);
        //if user chooses f
        }else if (option.equalsIgnoreCase("f")){
            //if paid amount == total amount
            if(Alpha.getPaidFee() != Alpha.getTotalAmount()){
                double OutStanding = Alpha.getTotalAmount() - Alpha.getPaidFee();
                //we show the users invoice
                System.out.println("Invoice:");
                System.out.println("Customer Details: "+Customer.getName()+
                    "\n\t\t\t\t"+Customer.getTelephoneNumber()
                    +"\n\t\t\t\t"+Customer.getPhysicalAddress()
                    +"\n\t\t\t\t"+Customer.getEmailAddress()
                    +"\nOutstanding amount: R"+OutStanding);}
            //else we print this
            else {
                System.out.println(Alpha);
                System.out.println("Project Finalized");
            }
        //if user chooses u
        }else if (option.equalsIgnoreCase("u")){
            System.out.println("Enter new Email Address here: ");
            Scanner Answer = new Scanner(System.in);
            String NewEmailAddress = Answer.nextLine();
            //we update the email address
            Contractor.setEmailAddress(NewEmailAddress);

            System.out.println("Enter new telephone number here: ");
            Answer = new Scanner(System.in);
            String NewPhoneNumber = Answer.nextLine();
            //we update the phone number
            Contractor.setTelephoneNumber(NewPhoneNumber);
            //we print the results
            System.out.println(Customer);
        }
    }
}

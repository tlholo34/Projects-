package com.company;

public class ACC {

    private String Name;
    private static String Surname;
    private String EmailAddress;
    private String TelephoneNumber;
    private String PhysicalAddress;

    public ACC(String name,String Surname,String emailAddress ,String telephoneNumber,String physicalAddress){
        this.Name = name;
        this.Surname = Surname;
        this.EmailAddress = emailAddress;
        this.TelephoneNumber = telephoneNumber;
        this.PhysicalAddress = physicalAddress;
    }

    public String getName() {
        return Name;
    }

    public static String getSurname() {
        return Surname;
    }

    public String getEmailAddress() {
        return EmailAddress;
    }

    public String getTelephoneNumber() {
        return TelephoneNumber;
    }

    public String getPhysicalAddress() {
        return PhysicalAddress;
    }

    public void setEmailAddress(String emailAddress) {
        EmailAddress = emailAddress;
    }

    public void setTelephoneNumber(String telephoneNumber) {
        TelephoneNumber = telephoneNumber;
    }
    //this puts all info into a string
    public String toString(){
        String outtie = "Name: "+ getName();
        outtie += "\nSurname: "+ getSurname();
        outtie += "\nEmail Address: "+ getEmailAddress();
        outtie += "\nTelephone number: "+ getTelephoneNumber();
        outtie += "\nPhysical Address: "+ getPhysicalAddress();
        outtie+= "\n";

        //we return the output
        return outtie;

    }

}
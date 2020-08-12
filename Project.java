package com.company;

public class Project{

    private String nameOfProject;
    private String ProjectNumber;
    private String Building;
    private String ProjectAddress;
    private String ERFNumber;
    private double TotalAmount;
    private double PaidFee;
    private String DeadLine;

    public Project(String nameOfProject,String projectNumber,String building,String projectAddress,String erfNumber,double paidFee,double totalAmount,String deadLine){
        this.nameOfProject = nameOfProject;
        this.ProjectNumber = projectNumber;
        this.Building = building;
        this.ProjectAddress = projectAddress;
        this.ERFNumber = erfNumber;
        this.PaidFee = paidFee;
        this.TotalAmount = totalAmount;
        this.DeadLine = deadLine;
    }

    public void setDeadLine(String d) {
        DeadLine = d;
    }

    public void setPaidFee(double paidFee) {
        PaidFee = paidFee;
    }

    public double getTotalAmount() {
        return TotalAmount;
    }

    public String getNameOfProject() {
        return nameOfProject;
    }

    public String getProjectNumber() {
        return ProjectNumber;
    }

    public String getBuilding() {
        return Building;
    }

    public String getProjectAddress() {
        return ProjectAddress;
    }

    public String getERFNumber() {
        return ERFNumber;
    }

    public double getPaidFee() {
        return PaidFee;
    }

    public String getDeadLine() {
        return DeadLine;
    }

    //this puts all info into a string
    public String toString(){
        String outtie = "Name of Project: "+ getNameOfProject();
        outtie += "\nProject number: "+ getProjectNumber();
        outtie += "\nBuilding Type: "+ getBuilding();
        outtie += "\nProject Address: "+ getProjectAddress();
        outtie += "\nERF number: "+ getERFNumber();
        outtie += "\nTotal amount Paid: R"+getPaidFee();
        outtie += "\nProject Fee: R"+ getTotalAmount() ;
        outtie += "\nDeadline: "+ getDeadLine();
        outtie+= "\n";

        //we return the output
        return outtie;
    }
}

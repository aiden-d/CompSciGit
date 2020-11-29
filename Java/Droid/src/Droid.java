public class Droid {
    private int batteryLevel;
    public Droid(){
        batteryLevel = 100;
    }
    public int getBatteryLevel(){
        return batteryLevel;
    }
    public void setBatteryLevel(int level){
        batteryLevel=level;
    }
    public Droid(int level){
        batteryLevel = level;
    }
    public void activate(){
        print("Activated. How can I help you?");
        batteryLevel -= 5;
        print("I am currently at "+batteryLevel+"% battery level");
    }
    public void chargeBattery(int hours){
        print("Droid charging....");
        if (hours*25+batteryLevel>100) batteryLevel=100;
        else batteryLevel=batteryLevel+(hours*25);
        print("I am currently at "+batteryLevel+"% battery level");
        if (batteryLevel==100){
            print("I am fully charged");
        }
        else {
            int hoursRemaining = Math.round((100-batteryLevel)/25);
            print(hoursRemaining + " hours until fully charged.");
        }


    }
    public boolean checkIfLowBatteryLevel(){
        print("I am currently at "+batteryLevel+"% battery level");

        if (batteryLevel<=10) return true;
        else return false;
    }
    public void hover(int feet){
        if (feet>2) print("Error! I cannot hover above 2 feet.");
        else print("Hovering....");
        batteryLevel -= 20;
        print("I am currently at "+batteryLevel+"% battery level");
    }


    public double Naman(double charge)
    {
        double currentCharge = batteryLevel;
        if (currentCharge<=100) batteryLevel = Math.round(Math.round(charge));
        return currentCharge;


    }


    public String toString() {
        return "Hi, I am a Droid and I am currently at "+batteryLevel+"% battery level";
    }
    private void print(String str){
        System.out.println(str);
    }

}

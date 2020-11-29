public class DriverClass {
    public static void main(String[] args) {
        Droid ReadyDroid = new Droid();
        Droid DeadDroid = new Droid(0);
        ReadyDroid.activate();
        DeadDroid.chargeBattery(5);
        ReadyDroid.hover(2);
        System.out.println(ReadyDroid.checkIfLowBatteryLevel());

    }
}

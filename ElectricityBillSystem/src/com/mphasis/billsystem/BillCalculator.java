package com.mphasis.billsystem;

public class BillCalculator {

	public static void main(String[] args) {
			int units = 280;
			double billTopay =0;
			if(units < 100)
			{
				billTopay = units * 1.20;
			}
			else if(units < 300)
			{
				billTopay = 160 * 1.20 + (units - 100) * 2;
			}
			System.out.println("The electricity bill for " +units+ "is : " + billTopay);
	}

}

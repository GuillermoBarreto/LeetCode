We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return true if we are in trouble.


monkeyTrouble(true, true) → true
monkeyTrouble(false, false) → true
monkeyTrouble(true, false) → false

//answer//

public boolean monkeyTrouble(boolean aSmile, boolean bSmile) {
    if (aSmile && bSmile) {
      return true;
    }
    if (!aSmile && !bSmile) {
      return true;
    }
    return false;
    // The above can be shortened to:
    //   return ((aSmile && bSmile) || (!aSmile && !bSmile));
    // Or this very short version (think about how this is the same as the above)
    //   return (aSmile == bSmile);
  }
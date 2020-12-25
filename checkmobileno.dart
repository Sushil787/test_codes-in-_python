//Program for identifying ncell/ntc no

import 'dart:io';

void main() {
  String number;
  print("Input the no you wanna check: ");
  number = stdin.readLineSync();
  var output = check(number);
  print(output);
}

String check(String number) {
  if (number.contains("980") |
      number.contains("981") |
      number.contains("982")) {
    return "its ncell no";
  } else if (number.contains("984") |
      number.contains("985") |
      number.contains("986")) {
    return "its ntc";
  } else if (number.contains("961") |
      number.contains("962") |
      number.contains("988")) {
    return "its smart cell";
  } else if (number.contains("974") |
      number.contains("975")) {
    return "its cdma/sky-sim";
  } else if (number.contains("972")) {
    return "its cdma by UTL";
  } else {
    return "its GSM";
  }
}

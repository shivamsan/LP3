//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank{

    address public accHolder;
    uint256 balance = 0;

    constructor(){
        accHolder  = msg.sender;

    }

    //0xd9145CCE52D386f254917e481eB44e9943F39138
    

    function withdraw() payable public {
        require(msg.sender == accHolder, "You are not the account owner.");
        require(balance > 0, "You dont have enough balance.");
        payable(msg.sender).transfer(balance);
        //balance = 0;
        balance -= msg.value;
    }

    function deposite() public payable {
        require(msg.sender == accHolder, "You are not the account owner.");
        require(msg.value > 0, "Deposite amount should be greater than 0.");
        balance += msg.value;

    }

    function showbalance() public view returns(uint) {
        require(msg.sender == accHolder, "You are not the account owner.");
        return balance;

    }
}


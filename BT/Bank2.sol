//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank{
    mapping (address=> uint256) balance;

    function withdraw(uint256 amount) public {
        require(amount > 0, "You dont have enough balance.");
        balance[msg.sender] -= amount;
    }

    function deposite(uint256 amount) public{
        require(amount > 0, "Deposite amount should be greater than 0.");
        balance[msg.sender] += amount;

    }

    function showbalance() public view returns(uint256) {

        return balance[msg.sender];

    }
}


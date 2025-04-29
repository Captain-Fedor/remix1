//SPDX-License-Itentifier: MIT
// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 < 0.9.0;

import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/shared/interfaces/AggregatorV3Interface.sol";


contract FundMe{

    address public owner;

    constructor()  {
        owner = payable(msg.sender);
    }
    
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;

    function fund() public payable {
        //uint256 minimunUSD = 50 * 10 ** 18;
        //require(getConversionRate(msg.value)>= minimunUSD, "revert error");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }
    
    function fundV2() public payable {
        require(getConversionRate(msg.value)>= getPrice(), "revert error");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
        (, int256 answer,,,) 
        = priceFeed.latestRoundData();
        
        return uint256(answer);
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    modifier onlyOwner {
        require (msg.sender == owner, "you are not the owner");
        _;

    }
    
    function withdraw() payable onlyOwner public {
        payable(msg.sender).transfer(address(this).balance);
        for(uint256 index = 0; index < funders.length;index++){
            address funder = funders[index];
           addressToAmountFunded[funder] = 0;  
        }
        funders = new address[](0);
        
    }


        //uint256 decimals = priceFeed.decimals();
        
       //   uint256 price = priceFeed.latestRoundData().answer * (10**(3 - decimals));  //rounding down to the nearest 8 decimal places

//to get latest price from chainlink feed     
//  function getPrice() public view returns(uint256) {
//         AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDcB523bF33D8A8A03dCC5);  //address of the Chainlink oracle
//         (, int256 answer,,,)  = priceFeed.latestRoundData();     
//          return uint256(answer * (10 **9));      
//     }
     
}
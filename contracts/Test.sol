pragma solidity ^0.6.0;


contract nestmap{
   mapping(uint => uint[]) public scores;
   function foo(uint spender) external{
      scores[spender].push(block.timestamp);
   }

}


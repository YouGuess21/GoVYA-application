import { useState } from "react";
import { Link } from "react-router-dom";
export default function Login(){
return(
<>
<div className="flex min-h-screen bg-dark-secondary  p-4">
<div className="m-auto w-full max-w-[1200px] px-2 sm:px-6 lg:px-8 ">
   <div className="flex flex-row items-center gap-[15%]">
      <div className="w-3/5 max-w-[450px]">
         <Link to="/">
         <button className=" text-dark-accent text-5xl font-bold hover:text-6xl hover:duration-100">GoVYA</button>
         </Link>
         <p className="mt-4 text-xl text-light-primary">GoVYA helps you connect and share with the people in your life.</p>
      </div>
      <div className="bg-light-primary p-10 pt-15 max-w-[425px] rounded-lg shadow-lg shadow-[#000000] w-3/5">
         <form className="flex flex-col gap-3 ">
            <input className=" bg-light-primary border-b border-placewhite focus:outline-none pb-1 mb-2" placeholder="Username" type="text" />
            <input className=" bg-light-primary border-b border-placewhite focus:outline-none pb-1" placeholder="Password" type="password" />
            <button className="bg-dark-accent text-light-primary rounded-md p-2 font-bold mt-4 mb-3">Log in</button>
         </form>
         <div className=" items-center flex flex-row justify-center">
            <p className="text-sm hover:underline" >
            Forgotten password?
            </p>
         </div>
         <div className="mt-10 flex justify-center ">
            <hr className=" w-full border-t border-placewhite" />
            </div>
            <div className="flex flex-row justify-center">
                <Link to="/signup" className="">
               <button className="bg-[#418ecd]  text-light-primary rounded-md p-3  mt-5 font-medium">Create new account</button>
                </Link>
            </div>
            
         </div>
      </div>
   </div>
</div>
</>
)
}

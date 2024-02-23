import { useState } from "react";
import { Link } from "react-router-dom";
export default function Signup(){
return(
<>
<div className="flex min-h-screen bg-dark-secondary p-4">
   <div className="m-auto w-full max-w-[1200px] px-2 sm:px-6 lg:px-8 ">
      <div className="flex flex-row items-center gap-[15%]">
         <div className="w-3/5 max-w-[450px]">
            <Link to="/">
            <button className="text-dark-accent text-5xl font-bold hover:text-6xl hover:duration-100">GoVYA</button>
            </Link>
            <p className="mt-4 text-xl text-light-primary text-justify">Create a new account on GoVYA to connect and share with others.</p>
         </div>
         <div className="bg-light-primary p-10 pt-15 max-w-[425px] rounded-lg shadow-lg shadow-[#000000] w-3/5">
            <form className="flex flex-col gap-3">
               <input className="bg-light-primary border-b border-placewhite focus:outline-none pb-1 mb-2" placeholder="Username" type="text" />
               <input className="bg-light-primary border-b border-placewhite focus:outline-none pb-2" placeholder="Password" type="password" />
               <input className="bg-light-primary border-b border-placewhite focus:outline-none pb-1 pt-2" placeholder="Email" type="email" />
               <button className="bg-dark-accent text-light-primary rounded-md p-2 font-bold mt-4 mb-3">Sign Up</button>
            </form>
            <div className="items-center flex flex-row justify-center">
               <p className="text-sm" >
                  Already have an account? 
                  <Link to="/login" className="pl-1 hover:underline">
                   Log in.</Link>
               </p>
            </div>
            
         </div>
      </div>
   </div>
</div>
</>
)
}
